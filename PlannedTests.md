# Tests ideas based on OpenAPI declaration

## Introduction

OpenAPI declaration tells 
* path
* http_methods
* parameters, each having
* * Type
* * Required/optional
* * nullable 
* * The way parameter is provided (path/query/header/cookie)

This information can be used to generathe automated tests. Ideas of possible tests are described in this document.

## type - dependent tests

Data Types in OpenAPI declaration:
https://swagger.io/docs/specification/data-models/data-types/

### string
properties to be used for tests generation:
* minLength (positive: matching, equal; negative: below minimal)
* maxLength (similar)
* format or pattern (e.g. email, name, id, uuid, date, filename, long text, number-as-string, case sensitivity, etc. => positive and negative tests)
* [enum](https://swagger.io/docs/specification/data-models/enums/)
* Allowed characters set  (  => positive and negative tests)
* * Disallowed characters

Additionally
* empty value
* NULL
* Leading and Trailing whitespaces

### number

* Minimum/exclusiveMinimum <br> (matching, equal, below minimal)
* Maximum/exclusiveMaximum (similarly)
* [multipleOf] 
* exclusiveMinimum: true
* float/double format
* E+ and e- with decimal degree

### integer
properties to be used for tests generation:
* Minimum/exclusiveMinimum <br> (matching, equal, below minimal)
* Maximum/exclusiveMaximum (similarly)
* zero (may be positive or negative)
* 
Additionally 
* Not-a-number (parsing error)
* Not-an-integer (parsing error)
* empty
* NULL
* negative number
* heading zero - not to impact
* [multipleOf]

### boolean

* true
* false
* NULL
* missing

### array

* items type


### object
