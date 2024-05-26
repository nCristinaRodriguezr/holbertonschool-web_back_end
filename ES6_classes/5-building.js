export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}

class OfficeBuilding extends Building {
  constructor(sqft, occupancy) {
    super(sqft);
    this._occupancy = occupancy;
  }

  evacuationWarningMessage() {
    return `Evacuate the building! Occupancy: ${this._occupancy}`;
  }
}

// Permitir la instancia de la clase Building
Building.prototype.evacuationWarningMessage = function() {
  throw new Error('Class extending Building must override evacuationWarningMessage');
};
