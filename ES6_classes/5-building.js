export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}

class TestBuilding extends Building {
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}

const b = new Building(100);
console.log(b);

try {
  new TestBuilding(200);
} catch (err) {
  console.log(err);
}
