# structural cycle and dead-step detection

Exact-repeat rules miss A-B-A-B cycles and steps whose output never changes later actions; a windowed fingerprint over the last several calls would catch them.
