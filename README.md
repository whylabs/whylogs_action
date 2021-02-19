# Hello world docker action

This action runs Whylog constraints on a static dataset.

## Inputs

### `constraintsfile`

**Required** Name of file holding JSON-encoded constraints.

### `datafile`

**Required** File holding feature data.  Format is anything that pandas package can load, likely CSV.

## Example usage

uses: whylogs-actions/action@v1
with:
  constraintsfile: 'constraints.json'
  datafile: 'lending_club_1000.csv'
