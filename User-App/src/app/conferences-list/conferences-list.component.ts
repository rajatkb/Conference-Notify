import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Conference } from '../models/conference.model';
import { ConferencesService } from '../services/conferences.service';

@Component({
  selector: 'app-conferences-list',
  templateUrl: './conferences-list.component.html',
  styleUrls: ['./conferences-list.component.css']
})


export class ConferencesListComponent implements OnInit {
public conferences: Conference[];
constructor(private http: HttpClient, public conferencesservice: ConferencesService) { }

ngOnInit() {
  this.conferences = this.conferencesservice.getConferences();
  }

}
