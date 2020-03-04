import { Conference } from '../schemas/conferences'
import { ConferenceModel } from '../models/conference';

export abstract class ConferenceController {


    constructor(private conferenceModel:ConferenceModel){ }

    abstract getConferences(offset:Number , count:Number):Array<Conference>;
    abstract getConferences(category:String , offset:Number , count:Number):Array<Conference>;
    abstract getCategories():Array<String>;
}