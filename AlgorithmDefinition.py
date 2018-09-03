pybites cheat sheet:
https://gallery.mailchimp.com/822043293f280259d4b8d2a3e/files/fa85b60d-3713-47e7-a7b4-5542d463d2fe/pybites_cheatsheet.pdf

function Backtracking_search(csp) returns solution or failure

function Backtrack(assignment, csp)
returns solution or failure

    if assignment is complete hen return assignment
        var = select_unassigned_variables(csp)
        for each value in order_domain_values(var, assignment, csp)
            if value is consistent with assignment then
                add {var = value} to assignment
                result = Backtrack(assignment, csp)
                if (result Not Equal failure) then return result
                remove {var = value} from assignment
         end for
         return failure