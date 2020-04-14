import { Component, OnInit, OnDestroy, HostListener } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Conference } from '../models/conference.model';
import { ConferencesService } from '../services/conferences.service';

@Component({
  selector: 'app-conferences-list',
  templateUrl: './conferences-list.component.html',
  styleUrls: ['./conferences-list.component.css']
})


export class ConferencesListComponent implements OnInit, OnDestroy {
public conferences: Conference[];
offset = 0;
count = 3;
constructor( public conferencesservice: ConferencesService) { }

@HostListener('window:scroll', ['$event'])
    scrollHandler(event) {
      console.log('Scroll Event');
      console.log(this.offset, this.count);
      this.getConferenceslist(this.offset, this.count);
    }

ngOnInit() {
  this.getConferenceslist(this.offset, this.count);
  }

  getConferenceslist(offSet, Count) {
    this.conferences = this.conferencesservice.getConferences(offSet, Count);
    this.offset += this.count;
    this.count += this.count;
  }
  ngOnDestroy() {

  }

}
