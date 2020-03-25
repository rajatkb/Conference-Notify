import { ConferenceModel } from "../../models/conference";
import { Stream } from '../../stream'
import { Observable } from "rxjs";
import { injectable } from "inversify";

/**
 * Stream for Conference model , responsible for creating
 * constant update stream for the Conference table/collection in database
 * 
 *
 * @export
 * @abstract
 * @class ConferenceStream
 * @implements {Stream}
 */
@injectable()
export abstract class ConferenceStream implements Stream{
    constructor(private conferenceModel:ConferenceModel){}
    abstract getStream():Observable<any>
}