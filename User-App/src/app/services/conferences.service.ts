import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Conference } from '../models/conference.model';

@Injectable({
  providedIn: 'root'
})
export class ConferencesService {
  constructor(private http: HttpClient) { }

  getConferences(offset, count) {
    const conferences: Conference[] = [];
    this.http.get('http://localhost:3000/conferences/' + offset + '/' + count).subscribe((conference) => {
      const key = 'payload';
      conference[key].forEach(
        val => {
          conferences.push(val);
        }
      );
    });
    return conferences;
  }

  getConference() {
    const conference: Conference[] = [];
    this.http.get('http://localhost:3000/conferences/getone').subscribe(conferenceobj => {
      const key = 'payload';
      conference.push(conferenceobj[key]);
    });
    return conference;
  }
}
