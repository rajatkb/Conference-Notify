import { Component, OnInit } from '@angular/core';
import { ConferencesService } from '../services/conferences.service';
import { Conference } from '../models/conference.model';

@Component({
  selector: 'app-conference',
  templateUrl: './conference.component.html',
  styleUrls: ['./conference.component.css']
})
export class ConferenceComponent implements OnInit {
  public conference: Conference[];
  constructor(public conferencesservice: ConferencesService) { }

  ngOnInit(): void {
    this.conference = this.conferencesservice.getConference();
  }

}
