import { Express , Request , Response } from 'express';

export abstract class Conference{
    
    private app:Express;
    
    constructor(app:Express){
        this.app = app;
    }
 
    /**
     *
     * /listConference/{offset}/{count}
     * @abstract
     * @param {Number} offset , offset of data item
     * @param {Number} count , count of data item requested
     * @param {Request} request 
     * @param {Response} response
     * @memberof Conference
     */
    abstract listConference(offset:Number, count:Number):void;

    /**
     *
     * /listConference/{category}/{count}
     * 
     * @abstract
     * @param {String} category
     * @param {Number} offset , offset of data item
     * @param {Number} count , count of data item requested
     * @param {Request} request 
     * @param {Response} response
     * @memberof Conference
     */
    abstract listConference(category:String , offset:Number , count:Number):void;



    /**
     *
     * /listCategory
     * 
     * @abstract
     * @param {Request} request
     * @param {Response} response
     * @memberof Conference
     */
    abstract listCategory():void;
 

}