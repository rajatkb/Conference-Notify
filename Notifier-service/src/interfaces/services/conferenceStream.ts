import { ConferenceModel } from "../models/conference";
import { Stream } from '../stream'
import { Observable } from "rxjs";
import { injectable } from "inversify";

@injectable()
export abstract class ConferenceStream implements Stream{
    constructor(private conferenceModel:ConferenceModel){}
    abstract getStream():Observable<any>
}