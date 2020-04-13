import { TestBed } from '@angular/core/testing';

import { ConferencesService } from './conferences.service';

describe('ConferencesService', () => {
  let service: ConferencesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ConferencesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
