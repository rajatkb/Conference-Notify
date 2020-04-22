import { ConferenceService } from '../interfaces/services/conference'
import { ConferenceModel } from '../interfaces/models/conference'
import { Conference, mongoQueryType } from '../schemas/conferences';
import { Logger } from '../utility/log';
import { injectable } from 'inversify';
import { ConferenceModelMongo } from '../models/conference';


@injectable()
export class ConferenceServiceI extends ConferenceService {
    private logger = new Logger(this.constructor.name).getLogger()
    constructor(private conferenceModel: ConferenceModel,
                private conferenceModelMongo:ConferenceModelMongo) {
        super()
    }
    async getOne(_id: string): Promise<Conference | null> {
        this.logger.debug("getOne invoked")
        let queryObj: mongoQueryType = {}
        queryObj['_id'] = _id
        return new Promise<Conference | null>((resolve, reject) => {
            this.conferenceModelMongo.getOne(queryObj).then((value)=>{
                if(value == null){
                    resolve(null)
                }else{
                    let conference: Conference = value.toObject()
                    resolve(conference)
                }
            },(error)=>{
                this.logger.error("getOne retrieval failed: " + error)
                reject(error)
            })
        })

    }


    async getConferences(offset:number , count:number):Promise<Conference[]>{
        this.logger.debug("getConferences invoked")
        return new Promise<Conference[] | []>((resolve , reject) => {
            this.conferenceModel.getConferences(offset, count).then( value => {
                if(value == []){
                    resolve([])
                }
                else{
                    let conference:Conference[] = value!?.map(val => val.toObject()); 
                    resolve(conference)
                }
            }).catch(err => {
                this.logger.error("getConferences retrieval failed: "+ err)
                reject(err)
            })
        }) 
    }
    
    async getConferencesFromCategory(category:string , offset:number , count:number):Promise<Conference[]>{
        this.logger.debug("getConferencesFromCategory invoked")
        return new Promise<Conference[] | []>((resolve , reject) => {
            this.conferenceModel.getConferencesFromCategory(category, offset, count).then( value => {
                if(value == []){
                    resolve([])
                }
                else{
                    let conference:Conference[] = value!?.map(val => val.toObject()); 
                    resolve(conference)
                }
            }).catch(err => {
                this.logger.error("getConferencesFromCategory retrieval failed: "+ err)
                reject(err)
            })
        }) 
    }

    async getCategories():Promise<Array<string>>{
        this.logger.debug("getCategories invoked")
        return new Promise<string[] | []>((resolve , reject) => {
            this.conferenceModel.getCategories().then( value => {
                if(value == []){
                    resolve([])
                }
                else{
                    let conference:string[] = value!;
                    resolve(conference)
                }
            }).catch(err => {
                this.logger.error("getCategories retrieval failed: "+ err)
                reject(err)
            })
        }) 
    }
}