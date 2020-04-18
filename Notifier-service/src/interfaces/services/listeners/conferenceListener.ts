import { injectable } from "inversify";
import { ConferenceStream } from "../streams/conferenceStream";
import { Listener } from "../../listener";

/**
 * Attaches the listeners to ConferenceStream
 * through callbacks or through event pipes/triggers
 *
 * @export
 * @abstract
 * @class ConferenceListener
 * @extends {Listener}
 */
@injectable()
export abstract class ConferenceListener extends Listener{
    constructor(private conferenceStream:ConferenceStream){
        super(conferenceStream)
    }
}