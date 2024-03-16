# 0x19-postmortem
 postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.
## Task 0:

### _Issue Summary:_

Between Tuesday, March 5, 2024, 10:30 UTC, and Wednesday, March 6, 2024, 03:00 UTC, our primary web application experienced an intermittent outage, affecting about 35% of our users. The key impact was a severe slowdown in service response times, resulting in an inability to access crucial features for the affected users. The root cause was traced to a memory leak in one of our backend services.

### _Timeline:_

Mar 5, 10:30 UTC — Issue detection through automated performance monitoring alerts, signaling a sharp increase in service response times.
Mar 5, 10:35 UTC — Initial assumption was a sudden surge in traffic or a DDoS attack. The engineering team started investigating network logs and traffic patterns.
Mar 5, 12:00 UTC — Investigation revealed normal traffic patterns and no signs of DDoS, leading the team down a misleading path.
Mar 5, 13:30 UTC — The incident was escalated to the senior backend engineers as the slowdown persisted.
Mar 5, 16:00 UTC — Detailed system diagnostics revealed abnormal memory consumption in a backend service.
Mar 6, 01:00 UTC — The problematic service was isolated, and a memory leak was identified as the root cause.
Mar 6, 03:00 UTC — A patch was deployed to fix the memory leak, resolving the incident.

### _Root Cause and Resolution:_

The issue was caused by a memory leak in one of our backend services. This service, crucial for most of the application’s operations, began consuming memory at an abnormal rate, leading to a slowdown in response times as the system struggled to manage resources.

Upon identification of the offending service, the team used specific debugging tools to trace and isolate the memory leak. The error was found in a recently deployed code update, where objects were not being correctly disposed of after use. A patch was created to fix this memory management issue and was promptly deployed, fixing the memory leak.

### _Corrective and Preventative Measures:_

Moving forward, several improvements are required to prevent such incidents:

Code Reviews: Enhance code review practices to flag potential memory management issues before deployment.
Automated Testing: Implement automated testing that includes memory leak detection.
Monitoring: Improve system monitoring to detect abnormal memory usage and trigger alerts earlier.

### _Specific tasks to address these improvements:_

Conduct a review of the current code review practices and update the guidelines to emphasize memory management.
Research and select a suitable automated testing tool with memory leak detection capabilities. Train the team to use this tool.
Update the monitoring system to include specific alerts for abnormal memory usage. Test the new alerts to ensure they work as expected.

## Task 1:

![Memory leaks](https://thumbs2.imgbox.com/uAUtBCnJ)

### _Issue Summary:_

It’s a regular Tuesday, March 5, 2024, at 10:30 UTC. Our web application, the digital darling of our users, decides to take a leisurely stroll instead of its usual sprint. This unexpected slowdown lasts until Wednesday, March 6, 2024, 03:00 UTC, causing a bit of a ruckus for 35% of our users. The culprit? A sneaky memory leak in one of our backend services.

### _Timeline:_

Imagine a timeline, like a heartbeat monitor in a hospital drama, with peaks and troughs representing our journey through this incident:

Mar 5, 10:30 UTC — Our digital canary starts singing about a spike in service response times.

Mar 5, 10:35 UTC — We suspect a traffic surge or a DDoS attack. Our engineers dive into the network logs.

Mar 5, 12:00 UTC — Traffic patterns are normal. Our DDoS theory sinks like a stone.

Mar 5, 13:30 UTC — We call in the senior backend engineers as our app continues to dawdle.

Mar 5, 16:00 UTC — System diagnostics reveal a backend service hogging memory like it’s going out of style.

Mar 6, 01:00 UTC — We corner the guilty service and identify a memory leak as the culprit.

Mar 6, 03:00 UTC — We deploy a patch, the memory leak is plugged, and service resumes its usual sprint.


### _Root Cause and Resolution:_

Our villain was a memory leak in a key backend service. It started to gobble up memory, causing our app to slow down as the system got overwhelmed.

Once we identified the memory-guzzling service, our engineering superheroes used their debugging tools to trace and isolate the leak. The leak was traced to a new code update where some data objects were partying non-stop instead of exiting gracefully when done. A quick patch was conjured up and deployed, ensuring the memory leak was a thing of the past.

### _Corrective and Preventive Measures:_

Lessons learned and a plan of action for the future:

Code Reviews: Make them more rigorous than a drill sergeant’s morning inspection, with a keen eye for potential memory management issues.

Automated Testing: Incorporate memory leak detection. It’s like a smoke alarm, but for code.

Monitoring: Beef up system monitoring to sniff out abnormal memory usage faster than a bloodhound on a trail.

### _To-do list:_

Review and update code review practices, focusing on memory management like a hawk.

Hunt down a robust automated testing tool that can spot a memory leak from a mile off. Train the team to be just as sharp.

Amp up the monitoring system with specific alerts for abnormal memory usage. Test these new alerts until they’re as reliable as a Swiss watch.

