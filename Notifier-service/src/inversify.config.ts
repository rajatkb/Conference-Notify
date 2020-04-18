import { Container } from "inversify";
import { Database } from "./interfaces/database";
import { MongoDb } from "./database/mongodb";
import { ConferenceModel } from "./interfaces/models/conference";
import { ConferenceModelMongo } from "./models/conference";
import { ConferenceServiceI } from "./services/conference";
import { ConferenceService } from "./interfaces/services/conference";
import { ConferenceController } from "./controllers/conference";
import { Route } from "./interfaces/route";
import { ConferenceRoute } from "./routes/conference";
import { ConferenceStream } from "./interfaces/services/streams/conferenceStream";
import { ConferenceStreamMongo } from "./services/streams/conferenceStream";
import { Listener } from "./interfaces/listener";
import { ConferenceListenerMongo } from "./services/listeners/conferenceListener";



export class AppContainer{
    private container:Container;
    constructor(){
        this.container = new Container()
        this.container.bind<Database>(Database).to(MongoDb).inSingletonScope();
        this.container.bind<ConferenceModel>(ConferenceModel).to(ConferenceModelMongo).inSingletonScope();
        this.container.bind<ConferenceService>(ConferenceService).to(ConferenceServiceI).inSingletonScope();
        this.container.bind<ConferenceController>(ConferenceController).to(ConferenceController).inSingletonScope();
        this.container.bind<Route>(Route).to(ConferenceRoute).inSingletonScope();
        this.container.bind<ConferenceStream>(ConferenceStream).to(ConferenceStreamMongo).inSingletonScope();
        this.container.bind<Listener>(Listener).to(ConferenceListenerMongo).inSingletonScope();
    }

    public getRoutes():Route[]{
        return this.container.getAll<Route>(Route)
    }

    public getListeners():Listener[]{
        return this.container.getAll<Listener>(Listener)
    }
    public getDatabase():Database{
        let databaseobj=this.container.get(Database);
        return databaseobj;
    }
}
