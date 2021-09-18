Changelog 

V0.3
- Done
    - Added time stack axis
    - Display function updated
    - Video limit using time duration
    - Logs will tell the duration of video written, for human help
- Pending
    - Getting the frame out
    - Convert into class form
    - Axis 3 - shuffle in the middle

V0.2 
- Done 
    - If its q or Q it will work well to exit the code
    - Multiple videos can be added to stack now
    - Size fixed for single video via parameter, Giving the option to choose the size of video for user
    - Limit_video index added - that video which will close the code None - infinite code run
    - Video writer - when video is over - write the video in the end (if that doesn't work well - we will make it to write continuously
    - If fps is fixed - thats fine who cares | if fps not fixed - calculate the fps for video
    - Author name changed, gif added, gif created, image uploaded to git, 
    - added MIT licence so anyone can contribute and use the product https://choosealicense.com/licenses/mit/
- Pending
    - Fixing the size of output video by user - done
    - Write one function to loop in the videos and generate frame - thats it - and keep other functions to get input as frame and perform the actions - so if someone wants specific thing - cool they can do that - if not then use the default function - it will use too much ram
    - Time based - enter the time in seconds after that it will break the video writing easy but cool - done
    - Next time
    - Tqdm as requirement to be added
    - Sending frame out to be used
    - Converting it to class - to enable frame wise stacking - if you want to do directly do hstack vstack - why using this thing?
    - Grid based output or people can repeat the activity twice
    - Or I can do it for them, run 2 functions in 1 function - find the size - and use it 
    - Axis 3 = when one frame of one and another of other - thats easy - just append the frame directly into the main stack of frames - run the adding thing twice and both frames will be added at once. - done

V0.1 
- Added 
    - Video is streaming so to watch the output
    - Vstack and hstack is added as axis 0 and 1
    - q to stop the processing is added
- Future Addition
    - It cant work with more than 2 videos - solved
    - Getting the frame out, is not possible
    - Using the frame as input to create a combined output 
    - Writing the videos if user passes the path - done
    - Choose which video time to be taken as end of video - done
