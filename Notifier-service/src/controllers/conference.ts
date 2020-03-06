import { Conference } from '../schemas/conferences'
import { ConferenceModel } from '../models/conference';
import { Controller } from '../controllers/controller';

export abstract class ConferenceController extends Controller {
    constructor(private conferenceModel:ConferenceModel){
        super(conferenceModel)

     }
    abstract getConferences(offset:Number , count:Number):Array<Conference> ;
    abstract getConferences(category:String , offset:Number , count:Number):Array<Conference>;
    abstract getCategories():Array<String>;
}