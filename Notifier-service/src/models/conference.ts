import mongoose from 'mongoose';
import { Connection } from 'mongoose';
import { Conference, ConferenceDocument, ConferenceSchema } from '../schemas/conferences';
import { Database } from '../interfaces/database';
import { ConferenceModel } from '../interfaces/models/conference';
import { Logger } from '../utility/log';



export class ConferenceModelI extends ConferenceModel {
    modelName = "conference"
    private model: Promise<mongoose.Model<ConferenceDocument, {}>>;
    private connection: Promise<Connection>;
    private logger = new Logger(this.constructor.name).getLogger();
    constructor(database: Database) {
        super(database)
        this.connection = database.getConnection()
            .then((connection: Connection) => {
                return Promise.resolve(connection);
            })
            .catch((error) => {
                let errstring = "Failed at getting connection :" + error;
                this.logger.error(errstring);
                return Promise.reject(error);
            })

        this.model = this.connection
            .then((connection: Connection) => {
                let model = connection.model<ConferenceDocument>(this.modelName, ConferenceSchema);
                return Promise.resolve(model);
            })
            .catch((error) => {
                let errstring = "Failed at getting connection for model" + error;
                this.logger.error(errstring);
                return Promise.reject(error);
            })

    }

    private async  makeQuery<T>(callback: (model: mongoose.Model<ConferenceDocument, {}>) => Promise<T>): Promise<T> {
        return this.model
            .then(callback)
            .catch(error => {
                this.logger.debug("Failed at"+ callback.name + ": error:" + error);
                this.logger.error("Failed at" + callback.name + " : model must have failed to initialize , or something error :" + error);
                return Promise.reject(new Error("model failed to be initialised"));
            });
    }


    async getOne(): Promise<ConferenceDocument | null> {
        let result = this.makeQuery((model) => {
            return new Promise<ConferenceDocument | null>((resolve, reject) => {
                model.findOne({}, (err, res) => {
                    if (!err) {
                        resolve(res);
                    }
                    else {
                        reject(err);
                    }
                })
            })
        })
        return result
    }

    async getConferences(offset: number, range: number): Promise<ConferenceDocument[] | null> {

        let result = this.makeQuery((model) => {
            return new Promise<ConferenceDocument[] | null>((resolve, reject) => {
                model.find({ "deadline": { $gte: new Date() } })
                     .sort({ 'deadline': 1 }).skip(offset).limit(range).exec((err, res) => {
                            if (!err) {
                                resolve(res);
                            }
                            else {
                                reject(err);
                            }
                     })
            })
        })
        return result
    }

    async getConferencesFromCategory(category: string, offset: number, range: number): Promise<ConferenceDocument[] | null> {
        let result = this.makeQuery((model) => {
                return new Promise<ConferenceDocument[] | null>((resolve, reject) => {
                    model.find({ 'categories': { $in: [category] } , "deadline": { $gte: new Date() } })
                         .sort({ 'deadline': 1 }).skip(offset).limit(range).exec((err, res) => {
                             if (!err) {
                            resolve(res);
                        }
                        else {
                            reject(err);
                        }
                    })
                })
            })
        return result
    }

    async getCategories(): Promise<any> {
        let result = this.makeQuery((model) => {
                return new Promise<ConferenceDocument[] | null>((resolve, reject) => {
                    model.distinct(('categories'), (err, res) => {
                        if (!err) {
                            resolve(res);
                        }
                        else {
                            reject(err);
                        }
                    })
                })
            })
        return result
    }

}



