import { Metadata } from './metadata.model';

export class ConferenceDocument {
  title: string;
  url: string;
  deadline: Date;
  metadata?: {
      [tag: string]: Metadata
  };

  categories?: Array<string>;
  dateRange?: Array<Date>;
  finalDue?: string;
  location?: string;
  notificationDue?: Date;
  bulkText?: string; // optional field
}
