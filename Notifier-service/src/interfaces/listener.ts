import { Stream } from './stream'
import { injectable } from 'inversify';

/**
 * Listener class is reponsible for 
 * establising listeners for any sort of stream
 * from the observables provided
 *
 * @export
 * @abstract
 * @class Listener
 */
@injectable()
export abstract class Listener {
    constructor(stream: Stream){}
}