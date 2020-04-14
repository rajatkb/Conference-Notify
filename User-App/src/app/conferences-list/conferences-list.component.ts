import { Component, OnInit, OnDestroy, HostListener } from '@angular/core';
import { Conference } from '../models/conference.model';
import { ConferencesService } from '../services/conferences.service';

@Component({
  selector: 'app-conferences-list',
  templateUrl: './conferences-list.component.html',
  styleUrls: ['./conferences-list.component.css']
})

export class ConferencesListComponent implements OnInit, OnDestroy {
public conferences: Conference[] = [];
public conferenceList: Array<Conference[]> = [];
offset = 0;
count = 3;
constructor( public conferencesservice: ConferencesService) { }

@HostListener('window:scroll', ['$event'])
    scrollHandler(event) {
      this.getConferenceslist(this.offset, this.count);
    }

  ngOnInit() {
    this.getConferenceslist(this.offset, this.count);
  }

  getConferenceslist(offSet, Count) {
    this.conferenceList.push(this.conferencesservice.getConferences(offSet, Count));
    const len = this.conferenceList.length;
    let i = 0;
    while (i < len) {
      this.conferenceList[i].forEach(conference => {
        this.conferences.push(conference);
      });
      i = i + 1;
    }
    this.offset += this.count;
    this.count += this.count;
  }
  ngOnDestroy() {

  }

}
