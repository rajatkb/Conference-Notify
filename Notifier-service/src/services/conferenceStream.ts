import { Model } from "mongoose";
import { ConferenceModel } from "../interfaces/models/conference";
import { ConferenceDocument } from "../schemas/conferences";
import { injectable } from "inversify";
import { Logger } from "../utility/log";
import { Observable , Observer} from 'rxjs'
import { ConferenceStream } from "../interfaces/services/conferenceStream";


@injectable()
export class ConferenceStreamMongo extends ConferenceStream{

    private logger = new Logger(this.constructor.name).getLogger()
    private streamObs$?:Observable<any>
    constructor(conferenceModel:ConferenceModel){

        super(conferenceModel)
        console.log("Stream entered !")
        
        let changeStream =  conferenceModel.makeQuery(async (model:Model<ConferenceDocument, {}>) => {
            try{
                let stream = await model.watch()
                console.log("Stream captured")
                return Promise.resolve(stream)
            }catch(err){
                this.logger.error(`Failed to get a watch stream :${err}`)
                return Promise.reject(err)
            }
            
        })

        changeStream.then(stream => {
            stream.on( "change"  , next => {
                console.log(next) 
            })
        }).catch(error => {
           console.log(error)
        })

        // this.streamObs$ = Observable.create((observer:Observer<any>) => {
            
        // })

        // /*
        //     TEST CODE
        // */

        // let subscription = this.streamObs$.subscribe({
        //     next: (data) => console.log(data),
        //     error: (error) => console.log(error),
        //     complete: () => console.log("complete , watching !!")
        // })


    }

    public getStream():Observable<any> {
        return Observable.create((obs:any) => obs.next("hello"))
    }
    


} 