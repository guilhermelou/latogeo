import { Injectable, Pipe, PipeTransform } from '@angular/core';

@Pipe({
    name: 'filter'
})
export class FilterPipe implements PipeTransform {
    transform(items: Array<any>, filter: {[key: string]: any }): Array<any> {
        console.log(items);
        return items.filter(item => {
            let notMatchingField = Object.keys(
                filter).find(
					key => item[key].toLowerCase(
						).indexOf(filter[key].toLowerCase()) != -1);
            return notMatchingField; // true if matches all fields
        });
    }
}
