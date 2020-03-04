import { Metadata } from './metadata';

export interface Conference{
    _id:string;
    title:string;
    url:string;
    deadline:Date;
    metadata:{
        [tag:string]:Metadata
    };
    
    categories?:Array<string>;
    dataRange?:Array<Date>;
    finalDue?:string;
    location?:string;
    notificationDue?:Date;
    bulkTest?:string; // optional field
}