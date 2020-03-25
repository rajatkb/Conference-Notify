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




let container = new Container()
container.bind<Database>(Database).to(MongoDb).inSingletonScope();
container.bind<ConferenceModel>(ConferenceModel).to(ConferenceModelMongo).inSingletonScope();
container.bind<ConferenceService>(ConferenceService).to(ConferenceServiceI).inSingletonScope();
container.bind<ConferenceController>(ConferenceController).to(ConferenceController).inSingletonScope();
container.bind<Route>(Route).to(ConferenceRoute).inSingletonScope();
container.bind<ConferenceStream>(ConferenceStream).to(ConferenceStreamMongo).inSingletonScope();
container.bind<Listener>(Listener).to(ConferenceListenerMongo).inSingletonScope();


export { container }
