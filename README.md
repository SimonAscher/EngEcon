# EngEcon

This library contains a number of functions to aid with the economic analysis of engineering systems.

Currently, the following 3 types of functions are implemented:
- Currency conversion - convert between different currencies based on annual averages.
  - e.g. `convert_currency_annual_average`
- Present value/present worth conversion - convert annuity or future value cash flows to their present value equivalent.
  - e.g. `present_value`
- Plant scaling - implements both power scaling to account for the effects of economies of scale on different plant sizes and CEPCI (Chemical Engineering Plant Cost Index) scaling to account for changes in equipment and plant costs over time.
  - e.g. `power_scale` and `CEPCI_scale`