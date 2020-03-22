import { Model } from '../model';
import { ConferenceDocument } from '../../schemas/conferences';

/**
 *  The conference model that needs to be implemented  
 *  The implementation must follow specification and can use whichever
 *  database object it adheres to.
 * @export
 * @abstract
 * @class ConferenceModel
 * @extends {Model}
 */
export abstract class ConferenceModel extends Model{
    protected abstract modelName:string;
    abstract async getOne():Promise<ConferenceDocument | null>
    abstract async getConferences(offset:number , range:number):Promise<ConferenceDocument[] | null>
    abstract async getConferencesFromCategory(category:string , offset:number , range:number):Promise<ConferenceDocument[] | null>
    abstract async getCategories():Promise<Array<string> | null>
}