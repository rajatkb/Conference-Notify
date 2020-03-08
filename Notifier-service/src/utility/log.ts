import winston from 'winston';

const FileConfig = (filename:string) =>{ 
    return {
            level: process.env.LOG_LEVEL,
            filename: `${process.env.LOG_FOLDER}/${filename}.log`,
            handleExceptions: true,
            json: true,
            colorize: false,
            timestamp:true
        } 
}

const ConsoleConfig = {
    level: process.env.LOG_LEVEL,
    handleExceptions: true,
    colorize: true,
                timestamp: function () {
                    return (new Date()).toLocaleTimeString();
                },
    prettyPrint: true
}

winston.addColors({
    error: 'red',
    warn: 'yellow',
    info: 'cyan',
    debug: 'green'
});

export class Logger{


    private logger:winston.Logger; 
    constructor(filename:string){
        this.logger = winston.createLogger({
            level: process.env.LOG_LEVEL,
            format: winston.format.combine(
                winston.format.json(),
                winston.format.timestamp(),
                winston.format.colorize()
            ),
            transports: [
                new winston.transports.Console(ConsoleConfig),
                new winston.transports.File(FileConfig(filename))
            ]
        })
    }    

    getLogger():winston.Logger{
        return this.logger;
    }
    
}







