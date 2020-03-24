import {ConferenceModel} from '../models/conference'
import {Service} from '../services'
import { Conference } from '../../schemas/conferences'
import { injectable } from 'inversify'

@injectable()
export abstract class ConferenceService extends Service{

    abstract async getConferences(offset:Number , count:Number):Promise<Conference[]>;
    abstract async getConferencesFromCategory(category:String , offset:Number , count:Number):Promise<Conference[]>
    abstract async getCategories():Promise<Array<String>>

    abstract async getOne():Promise<Conference | null>
}