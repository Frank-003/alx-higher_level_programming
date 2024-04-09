#!/usr/bin/node
class Rectangle {
	constructor (w, h){
		if (w >= 0 && h >= 0) {
			this.width = w;
			this.height = h;
		}
	}
	print () {
	 for (let = 0; i < this.height; i++) {
		 console.log('X'.repeat(this.width));
	 }
	}
	rotate () {
		[this.width, this.height] = [this.height, this.width];
	}
	double () {
		this.width = this.height * 2;
		this.height = this.width * 2;
	}
}
