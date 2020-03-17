import { ConferenceService } from '../interfaces/services/conference'
import { ConferenceModel } from '../interfaces/models/conference'
import { Conference } from '../schemas/conferences';
import { Logger } from '../utility/log';

export class ConferenceServiceI extends ConferenceService{
    
    private logger = new Logger(this.constructor.name).getLogger()

    constructor(private conferenceModel:ConferenceModel){
        super()
    }
    
    async getOne():Promise<Conference | null>{
        this.logger.debug("getOne invoked")
        return new Promise<Conference | null>((resolve , reject) => {
            this.conferenceModel.getOne().then( value => {
                if(value == null){
                    resolve(null)
                }
                else{
                    let result = value.toObject()
                    let conference:Conference = result 
                    resolve(conference)
                }
            }).catch(err => {
                this.logger.error("getOne retrieval failed: "+ err)
                reject(err)
            })
        }) 
    }


    async getConferences(offset:Number , count:Number):Promise<Conference[]>{
        return Promise.resolve([])
    }
    async getConferencesFromCategory(category:String , offset:Number , count:Number):Promise<Conference[]>{
        return Promise.resolve([])
    }
    async getCategories():Promise<Array<String>>{
        return Promise.resolve([])
    }

}