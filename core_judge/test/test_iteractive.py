try:

    from ..job.OutputOnly import OutputOnly
    from ..job.iteractive import Iteractive

except:
    from job.OutputOnly import OutputOnly
    from job.iteractive import Iteractive
    from config import env

contestant_source = []
with open("/opt/problems_test/iteractive/wa_sol.cpp","r") as f:
    contestant_source = f.read()
print(contestant_source)
jobdescription = {
    # "multiprocess":,
    "time":1.,
    "contestant_source":contestant_source,
    "contestant_lang":"cpp",
    "checker":"/opt/problems_test/iteractive/checker.cpp",
    "iteractor":"/opt/problems_test/iteractive/iteractive.cpp",
    "iteractor_lang":"cpp",
    "checker_lang":"cpp",
    "inputs":"/opt/problems_test/iteractive/inputs",
    "outputs":"/opt/problems_test/iteractive/outputs",
    "type":"ioi",
    "sess":"submit",
}
job = Iteractive(jobdescription)
# job.prepare_file()
# print(job.sandbox_fifo_user_to_manager)
# job.compiler()
# job.run_per_test(1)
job.run()
job.eval_status()
job.sandbox.cleanup()
# job.sandbox.cleanup()
