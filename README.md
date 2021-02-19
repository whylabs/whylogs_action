# Whylogs constraint validation docker action

This action runs Whylog constraints on a static dataset.

## Inputs

### `constraintsfile`

**Required** Name of file holding JSON-encoded constraints.
Constraints assert that a boolean comparison during logging, or assert a boolean comparison on summary statistics.
Each constraint is bound to a column in the data.  Each column may have multiple constraints.
The supported boolean comparison operators are LT, LE, EQ, NE, GE, GT

For example, 
```
{
  "valueConstraints": {
    "fico_range_high": {
      "constraints": [
        {
          "name": "value GT 4000",
          "value": 4000.0,
          "op": "GT",
          "verbose": false
        }
      ]
    },
    "loan_amnt": {
      "constraints": [
        {
          "name": "value LT 548250",
          "value": 548250.0,
          "op": "LT",
          "verbose": false
        },
        {
          "name": "value LT 2500.0",
          "value": 2500.0,
          "op": "LT",
          "verbose": true
        }
      ]
    }
  },
  "summaryConstraints": {
    "annual_inc": {
      "constraints": [
        {
          "name": "summary min GE 0/None",
          "firstField": "min",
          "value": 0.0,
          "op": "GE",
          "verbose": false
        }
      ]
    }
  }
}
```


### `datafile`

**Required** File holding feature data.  Format is anything that pandas package can load, but CSV works well.

## Example usage

uses: whylogs-actions/action@v1
with:
  constraintsfile: 'constraints.json'
  datafile: 'lending_club_1000.csv'
