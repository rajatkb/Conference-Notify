import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-conferences-list',
  templateUrl: './conferences-list.component.html',
  styleUrls: ['./conferences-list.component.css']
})


export class ConferencesListComponent implements OnInit {

constructor(private http: HttpClient) { }

ngOnInit() {
    let conferences: any[];
    this.http.get('http://localhost:3000/conferences/0/10').subscribe((conference) => {
      conferences.push(conference);
    });
    console.log(conferences);
  }

}
