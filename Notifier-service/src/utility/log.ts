import winston from 'winston';

export class Logger{


    private logger:winston.Logger; 
    constructor(filename:string){
        this.logger = winston.createLogger({
            level: process.env.LOG_LEVEL,
            transports: [
                new winston.transports.Console({ format: winston.format.colorize({all:true}),}),
                new winston.transports.File({ filename: `${process.env.LOG_FOLDER}/${filename}.log` })
            ] , 

            format: winston.format.combine(
                         winston.format.label({
                            label: filename
                         }),
                         
                         winston.format.timestamp(),
                         winston.format.printf((info) => {
                             return `${info.timestamp} - ${info.label}:[${info.level}]: ${info.message}`;
                         })
                     )

        })
    }    

    getLogger():winston.Logger{
        return this.logger;
    }
    
}







