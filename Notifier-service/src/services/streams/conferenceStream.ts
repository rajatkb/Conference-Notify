import { Model } from "mongoose";
import { ConferenceModel } from "../../interfaces/models/conference";
import { ConferenceDocument } from "../../schemas/conferences";
import { injectable } from "inversify";
import { Logger } from "../../utility/log";
import { Observable, Observer } from 'rxjs'
import { share, filter } from 'rxjs/operators'

import { ConferenceStream } from "../../interfaces/services/streams/conferenceStream";


@injectable()
export class ConferenceStreamMongo extends ConferenceStream {

    private logger = new Logger(this.constructor.name).getLogger()
    private streamObs$: Observable<any>
    private insertstreamObs$: Observable<any>;
    private updatestreamObs$: Observable<any>;
    private deletestreamObs$: Observable<any>;
    private replacestreamObs$: Observable<any>;
    constructor(conferenceModel: ConferenceModel) {
        super(conferenceModel)
        this.logger.info("Conference Stream started")
        let changeStream = conferenceModel.makeQuery(async (model: Model<ConferenceDocument, {}>) => {
            try {
                let stream = await model.watch([] , {fullDocument: 'updateLookup'});
                return Promise.resolve(stream)
            } catch (err) {
                this.logger.error(`Failed to get a watch stream :${err}`)
                return Promise.reject(err)
            }
        })
        this.streamObs$ = Observable.create((observer: Observer<any>) => {
            changeStream.then(stream => {
                stream.on("change", (data:Object) => {
                    observer.next(data)
                })
            }).catch(error => {
                this.logger.error(`change stream failed:${error}`)
                observer.error(error)
                observer.complete()
            })
        })
            .pipe(
                share()
            )
        this.insertstreamObs$ = this.getStream().pipe(filter(data => {
            return data.operationType == 'insert'
        }))
        this.updatestreamObs$ = this.getStream().pipe(filter(data => {
            return data.operationType == 'update'
        }))
        this.deletestreamObs$ = this.getStream().pipe(filter(data => {
            return data.operationType == 'delete'
        }))
        this.replacestreamObs$ = this.getStream().pipe(filter(data => {
            return data.operationType == 'replace' 
        }))
            
        // this.insertstreamObs$ = Observable.create((observer: Observer<any>) => {
        //     changeStream.then(stream => {
        //         stream.on("insert", (data:Object) => {
        //             observer.next(data)
        //         })
        //     }).catch(error => {
        //         this.logger.error(`insert stream failed:${error}`)
        //         observer.error(error)
        //         observer.complete()
        //     })
        // })

        // this.updatestreamObs$ = Observable.create((observer: Observer<any>) => {
        //     changeStream.then(stream => {
        //         stream.on("update", (data:Object) => {
        //             observer.next(data)
        //         })
        //     }).catch(error => {
        //         this.logger.error(`update stream failed:${error}`)
        //         observer.error(error)
        //         observer.complete()
        //     })
        // })

        // this.deletestreamObs$ = Observable.create((observer: Observer<any>) => {
        //     changeStream.then(stream => {
        //         stream.on("delete", (data:Object) => {
        //             observer.next(data)
        //         })
        //     }).catch(error => {
        //         this.logger.error(`delete stream failed:${error}`)
        //         observer.error(error)
        //         observer.complete()
        //     })
        // })

        // this.replacestreamObs$ = Observable.create((observer: Observer<any>) => {
        //     changeStream.then(stream => {
        //         stream.on("replace", (data:Object) => {
        //             observer.next(data)
        //         })
        //     }).catch(error => {
        //         this.logger.error(`replace stream failed:${error}`)
        //         observer.error(error)
        //         observer.complete()
        //     })
        // })
    }

    public getStream(): Observable<any> {
        return this.streamObs$;
    }
    public getInsertStream():Observable<any> {
        return this.insertstreamObs$;
    }
    public getUpdateStream():Observable<any> {
        return this.updatestreamObs$;
    }
    public getDeleteStream():Observable<any> {
        return this.deletestreamObs$;
    }
    public getReplaceStream():Observable<any> {
        return this.replacestreamObs$;
    }


} 