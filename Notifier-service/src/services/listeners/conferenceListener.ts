import { ConferenceStream } from '../../interfaces/services/streams/conferenceStream'
import { injectable } from 'inversify';
import { Logger } from '../../utility/log';
import { ConferenceListener } from '../../interfaces/services/listeners/conferenceListener';

@injectable()
export class ConferenceListenerMongo extends ConferenceListener {

    private logger = new Logger(this.constructor.name).getLogger()
    
    constructor(conferenceStream:ConferenceStream)  {
        super(conferenceStream)
        this.logger.info("Conference Listener started")
        conferenceStream.getStream().subscribe({
            next: (data:Object) => {
                console.log(data)
                this.logger.debug(`recieving data from stream : ${JSON.stringify(data)}`)
            },
            error: (error) => this.logger.error(error),
            complete: () => this.logger.warn("Stream is detached and complete, should not happen !!")
        })
    }

}
