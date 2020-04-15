import mongoose from 'mongoose';
import { ConferenceDocument } from '../../schemas/conferences';
import { injectable } from 'inversify';
import { Model } from '../model';

/**
 *  The conference model that needs to be implemented  
 *  The implementation must follow specification and can use whichever
 *  database object it adheres to.
 * @export
 * @abstract
 * @class ConferenceModel
 * @extends {Model}
 */
@injectable()
export abstract class ConferenceModel extends Model{
    protected abstract modelName:string;
    abstract async getOne(query:any):Promise<ConferenceDocument | null>
    abstract async getConferences(offset:number , range:number):Promise<ConferenceDocument[] | null>
    abstract async getConferencesFromCategory(category:string , offset:number , range:number):Promise<ConferenceDocument[] | null>
    abstract async getCategories():Promise<Array<string> | null>
    abstract async makeQuery<T>(callback: (model: mongoose.Model<ConferenceDocument, {}>) => Promise<T>): Promise<T> 
}