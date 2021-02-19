# Whylogs constraint validation docker action

This action runs Whylog constraints on a static dataset.

## Inputs

### `constraintsfile`

**Required** Name of file holding JSON-encoded constraints.
Constraints assert that a logged value or summary statistic is within an expected range.
Each constraint is bound to a column in the data, and each column may have multiple constraints.
The standard boolean comparison operators are supported -- LT, LE, EQ, NE, GE, GT

For example, 
```
{
  "valueConstraints": {
    "loan_amnt": {
      "constraints": [
        {
          "value": 548250.0,
          "op": "LT"
        },
        {
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
          "firstField": "min",
          "value": 0.0,
          "op": "GE"
        }
      ]
    }
  }
}
```

Constraints may have an optional name to make them easier to identify.  
The name has no significance beyond labelling the constraint for reporting.   If not provided, a label is automatically constructed. 

Constraints may also be marked 'verbose' which will log every failure.
```
INFO - value constraint value GT 2500.0 failed on value 2500.0
```
Verbose logging helps identify why a constraint is failing to validate, but can be very chatty if there are a lot of failures.

Constraints are divided into two categories; value constraints and summary constraints.
Value constraints are applied to every value that is logged for a feature. At a minimum, 
Value constraints must specify a comparison operator and a literal value.
e.g. 
```
        {
          "op": "GT",
          "value": 4000.0
        },
        {
          "op": "LT",
          "value": 50000.0,
          "name": "Must not exceed",
          "verbose": true 
        },
        
```

Summary constraints are applied to Whylogs feature summaries, They compare fields of the summary to static literals or to another field in the summary,
e.g.    




### `datafile`

**Required** File holding feature data.  Format is anything that pandas package can load, but CSV works well.

## Example usage

uses: whylogs-actions/action@v1
with:
  constraintsfile: 'constraints.json'
  datafile: 'lending_club_1000.csv'
