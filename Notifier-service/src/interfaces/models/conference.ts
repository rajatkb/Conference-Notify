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

    /*
        TO-DO 
        getCategories may move to sepparate Model section , since it may require a sepparate 
        schema support of category
    */
    abstract async getCategories():Promise<any>
}