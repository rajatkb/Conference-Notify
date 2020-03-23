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


    async getConferences(offset:number , count:number):Promise<Conference[]>{
        this.logger.debug("getConferences invoked")
        return new Promise<Conference[] | []>((resolve , reject) => {
            this.conferenceModel.getConferences(offset, count).then( value => {
                if(value == []){
                    resolve([])
                }
                else{
                    let result = Object.assign({}, value);
                    let conference:Conference[] = result 
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
                    let result = Object.assign({}, value);
                    let conference:Conference[] = result 
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
                    let result = Object.assign({}, value);
                    let conference:string[] = result 
                    resolve(conference)
                }
            }).catch(err => {
                this.logger.error("getCategories retrieval failed: "+ err)
                reject(err)
            })
        }) 
    }

}