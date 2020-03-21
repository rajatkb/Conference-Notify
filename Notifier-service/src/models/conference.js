"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
exports.__esModule = true;
var conferences_1 = require("../schemas/conferences");
var conference_1 = require("../interfaces/models/conference");
var log_1 = require("../utility/log");
var ConferenceModelI = /** @class */ (function (_super) {
    __extends(ConferenceModelI, _super);
    function ConferenceModelI(database) {
        var _this = _super.call(this, database) || this;
        _this.modelName = "conference";
        _this.logger = new log_1.Logger(_this.constructor.name).getLogger();
        // this.connection = connection
        // this.model = this.connection.model<ConferenceDocument>( this.modelName, ConferenceSchema);
        _this.connection = database.getConnection()
            .then(function (connection) {
            return Promise.resolve(connection);
        })["catch"](function (error) {
            var errstring = "Failed at getting connection :" + error;
            _this.logger.error(errstring);
            return Promise.reject(error);
        });
        _this.model = _this.connection
            .then(function (connection) {
            var model = connection.model(_this.modelName, conferences_1.ConferenceSchema);
            return Promise.resolve(model);
        })["catch"](function (error) {
            var errstring = "Failed at getting connection for model" + error;
            _this.logger.error(errstring);
            return Promise.reject(error);
        });
        return _this;
    }
    ConferenceModelI.prototype.getOne = function () {
        return __awaiter(this, void 0, void 0, function () {
            var result;
            var _this = this;
            return __generator(this, function (_a) {
                result = this.model
                    .then(function (model) {
                    return new Promise(function (resolve, reject) {
                        model.findOne({}, function (err, res) {
                            if (!err) {
                                resolve(res);
                            }
                            else {
                                reject(err);
                            }
                        });
                    });
                })["catch"](function (error) {
                    _this.logger.debug("Failed at getOne: model not initialised error:" + error);
                    _this.logger.error("Failed at getOne : model must have failed to initialize :" + error);
                    return Promise.reject(new Error("model failed to be initialised"));
                });
                return [2 /*return*/, result];
            });
        });
    };
    /*
        TO-DO
    */
    ConferenceModelI.prototype.getConferences = function (offset, range) {
        return __awaiter(this, void 0, void 0, function () {
            var result;
            var _this = this;
            return __generator(this, function (_a) {
                result = this.model.then(function (model) {
                    return new Promise(function (resolve, reject) {
                        var response = model.find({ "deadline": { $gte: new Date() } }).sort({ 'deadline': -1 }).skip(offset).limit(range).map(function (data) {
                            data.map(function (val) {
                                var currentDate = Date.now();
                                var dateDiff = (val.deadline.getDate() - currentDate);
                                console.log("dateDifference : ", dateDiff);
                                return Object.assign(val, { dateDiff: dateDiff });
                            });
                        });
                        return (response);
                        // model.find({"deadline": {$gte: new Date()}}, (err, res) => {
                        //     if(!err) {
                        //         const response = res.map(data => {
                        //             let currentDate = Date.now();
                        //             let dateDiff = (data.deadline.getDate() - currentDate)
                        //             console.log("dateDifference : ",dateDiff);
                        //                     return Object.assign(data,{ dateDiff })
                        //         })
                        //         resolve(response);
                        //     }
                        //     else {
                        //         reject(err);
                        //     }
                        // }).sort({'deadline': -1}).limit(range);
                    });
                })["catch"](function (error) {
                    _this.logger.debug("Failed at getConferences: model not initialised error:" + error);
                    _this.logger.error("Failed at getConferences : model must have failed to initialize :" + error);
                    return Promise.reject(new Error("model failed to be initialised"));
                });
                return [2 /*return*/, result];
            });
        });
    };
    /*
        TO-DO
    */
    ConferenceModelI.prototype.getConferencesFromCategory = function (category, offset, range) {
        return __awaiter(this, void 0, void 0, function () {
            return __generator(this, function (_a) {
                return [2 /*return*/, Promise.resolve(null)];
            });
        });
    };
    ConferenceModelI.prototype.getCategories = function () {
        return __awaiter(this, void 0, void 0, function () {
            return __generator(this, function (_a) {
                return [2 /*return*/, Promise.resolve(null)];
            });
        });
    };
    return ConferenceModelI;
}(conference_1.ConferenceModel));
exports.ConferenceModelI = ConferenceModelI;
