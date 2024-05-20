# Avoid using tabs for indentation, use spaces.
# Don't use floats, they might break things.


# Combination Mode offsets
# ------------------------

TRACK_OFFSET = (
    -1
)  # offset from the left of linked session origin; set to -1 for auto-joining of multiple instances
SCENE_OFFSET = 0  # offset from the top of linked session origin (no auto-join)

# Buttons / Pads
# -------------
# Valid Note/CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments are permitted

BUTTONCHANNEL = 0  # Channel assignment for all mapped buttons/pads; valid range is 0 to 15 ; 0=1, 1=2 etc.
MESSAGETYPE = 0  # Message type for buttons/pads; set to 0 for MIDI Notes, 1 for CCs.
# When using CCs for buttons/pads, set BUTTONCHANNEL and SLIDERCHANNEL to different values.


# Track selection box (aka that coloured box for scene/track launching)
TSB_X = (
    64  # Controls the horizontal value for the track selection box. Default value is 8
)
TSB_Y = (
    1  # Controls the horizontal value for the track selection box. Default value is 8
)

# General
PLAY = -1  # Global play
STOP = -1  # Global stop
REC = -1  # Global record
TAPTEMPO = -1  # Tap tempo
NUDGEUP = -1  # Tempo Nudge Up
NUDGEDOWN = -1  # Tempo Nudge Down
UNDO = -1  # Undo
REDO = -1  # Redo
LOOP = -1  # Loop on/off
PUNCHIN = -1  # Punch in
PUNCHOUT = -1  # Punch out
OVERDUB = -1  # Overdub on/off
METRONOME = -1  # Metronome on/off
RECQUANT = -1  # Record quantization on/off
DETAILVIEW = -1  # Detail view switch
CLIPTRACKVIEW = -1  # Clip/Track view switch

# Device Control
DEVICELOCK = -1  # Device Lock (lock "blue hand")
DEVICEONOFF = -1  # Device on/off
DEVICENAVLEFT = -1  # Device nav left
DEVICENAVRIGHT = -1  # Device nav right
DEVICEBANKNAVLEFT = -1  # Device bank nav left
DEVICEBANKNAVRIGHT = -1  # Device bank nav right
DEVICEBANK = (
    -1,  # 
    -1,  # 
    -1,  # 
    -1,  # 
    -1,  # 
    -1,  # 
    -1,  # 
    -1,  # 
)

# Arrangement View Controls
SEEKFWD = -1  # Seek forward
SEEKRWD = -1  # Seek rewind

# Session Navigation (aka "red box")
SESSIONLEFT = -1  # Session left
SESSIONRIGHT = -1  # Session right
SESSIONUP = -1  # Session up
SESSIONDOWN = -1  # Session down
ZOOMUP = -1  # Session Zoom up
ZOOMDOWN = -1  # Session Zoom down
ZOOMLEFT = -1  # Session Zoom left
ZOOMRIGHT = -1  # Session Zoom right

# Track Navigation
TRACKLEFT = -1  # Track left
TRACKRIGHT = -1  # Track right

# Scene Navigation
SCENEUP = -1  # Scene down
SCENEDN = -1  # Scene up

# Scene Launch
SELSCENELAUNCH = -1  # Selected scene launch
SCENELAUNCH = (
    -1,  # Scene 1 Launch
    -1,  # Scene 2
    -1,  # Scene 3
    -1,  # Scene 4
    -1,  # Scene 5
    -1,  # Scene 6
    -1,  # Scene 7
    -1,  # Scene 8
    -1,  # Scene 9
    -1,  # Scene 10
    -1,  # Scene 11
    -1,  # Scene 12
    -1,  # Scene 13
    -1,  # Scene 14
    -1,  # Scene 15
    -1,  # Scene 16
    -1,  # Scene 17
    -1,  # Scene 18
    -1,  # Scene 19
    -1,  # Scene 20
    -1,  # Scene 21
    -1,  # Scene 22
    -1,  # Scene 23
    -1,  # Scene 24
    -1,  # Scene 25
    -1,  # Scene 26
    -1,  # Scene 27
    -1,  # Scene 28
    -1,  # Scene 29
    -1,  # Scene 30
    -1,  # Scene 31
    -1,  # Scene 32
    -1,  # Scene 33
    -1,  # Scene 34
    -1,  # Scene 35
    -1,  # Scene 36
    -1,  # Scene 37
    -1,  # Scene 38
    -1,  # Scene 39
    -1,  # Scene 40
    -1,  # Scene 41
    -1,  # Scene 42
    -1,  # Scene 43
    -1,  # Scene 44
    -1,  # Scene 45
    -1,  # Scene 46
    -1,  # Scene 47
    -1,  # Scene 48
    -1,  # Scene 49
    -1,  # Scene 50
    -1,  # Scene 51
    -1,  # Scene 52
    -1,  # Scene 53
    -1,  # Scene 54
    -1,  # Scene 55
    -1,  # Scene 56
    -1,  # Scene 57
    -1,  # Scene 58
    -1,  # Scene 59
    -1,  # Scene 60
    -1,  # Scene 61
    -1,  # Scene 62
    -1,  # Scene 63
    -1,  # Scene 64
)

# Clip Launch / Stop
SELCLIPLAUNCH = -1  # Selected clip launch
STOPALLCLIPS = -1  # Stop all clips

# 64X64 Matrix note assignments
CLIPNOTEMAP = (
#     1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32 33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 1
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 2
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 3
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 4
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 5
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 6
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 7
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 8
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 9
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 10
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 11
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 12
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 13
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 14
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 15
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 16
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 17
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 18
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 19
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 20
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 21
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 22
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 23
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 24
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 25
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 26
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 27
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 28
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 29
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 30
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 31
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 32
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 33
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 34
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 35  
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 36
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 37
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 38
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 39
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 40
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 41
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 42
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 43
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 44
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 45
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 46
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 47
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 48
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 49
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 50
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 51
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 52
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 53
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 54
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 55
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 56
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 57
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 58
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 59
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 60
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 61
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 62
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 63
    (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),  # Row 64
)

# Track Control
MASTERSEL = -1  # Master track select
SELTRACKREC = -1  # Arm Selected Track
SELTRACKSOLO = -1  # Solo Selected Track
SELTRACKMUTE = -1  # Mute Selected Track

TRACKSTOP = (
    -1,  # Pink Track 1
    -1,  # Pink Track 2
    -1,  # Pink Track 3
    -1,  # Pink Track 4
    -1,  # Pink Track 5
    -1,  # Pink Track 6
    -1,  # Pink Track 7
    -1,  # Pink Track 8
    -1,  # Pink Track 9
    -1,  # Pink Track 10
    -1,  # Pink Track 11
    -1,  # Pink Track 12
    -1,  # Pink Track 13
    -1,  # Pink Track 14
    -1,  # Pink Track 15
    -1,  # Pink Track 16
    -1,  # Green Track 17
    -1,  # Green Track 18
    -1,  # Green Track 19
    -1,  # Green Track 20
    -1,  # Green Track 21
    -1,  # Green Track 22
    -1,  # Green Track 23
    -1,  # Green Track 24
    -1,  # Green Track 25
    -1,  # Green Track 26
    -1,  # Green Track 27
    -1,  # Green Track 28
    -1,  # Green Track 29
    -1,  # Green Track 30
    -1,  # Green Track 31
    -1,  # Green Track 32
    -1,  # Yellow Track 33
    -1,  # Yellow Track 34
    -1,  # Yellow Track 35
    -1,  # Yellow Track 36
    -1,  # Yellow Track 37
    -1,  # Yellow Track 38
    -1,  # Yellow Track 39
    -1,  # Yellow Track 40
    -1,  # Yellow Track 41
    -1,  # Yellow Track 42
    -1,  # Yellow Track 43
    -1,  # Yellow Track 44
    -1,  # Yellow Track 45
    -1,  # Yellow Track 46
    -1,  # Yellow Track 47
    -1,  # Yellow Track 48
    -1,  # Blue Track 49
    -1,  # Blue Track 50
    -1,  # Blue Track 51
    -1,  # Blue Track 52
    -1,  # Blue Track 53
    -1,  # Blue Track 54
    -1,  # Blue Track 55
    -1,  # Blue Track 56
    -1,  # Blue Track 57
    -1,  # Blue Track 58
    -1,  # Blue Track 59
    -1,  # Blue Track 60
    -1,  # Blue Track 61
    -1,  # Blue Track 62
    -1,  # Blue Track 63
    -1,  # Blue Track 64
)

# The tracks are orderded in the same way as the launchpad drums view 4 x 4x4 grid: pink, green, yellow, blue.
TRACKSEL = (
    64,  # Pink Track 1
    65,  # Pink Track 2
    66,  # Pink Track 3
    67,  # Pink Track 4
    60,  # Pink Track 5
    61,  # Pink Track 6
    62,  # Pink Track 7
    63,  # Pink Track 8
    56,  # Pink Track 9
    57,  # Pink Track 10
    58,  # Pink Track 11
    59,  # Pink Track 12
    52,  # Pink Track 13
    53,  # Pink Track 14
    54,  # Pink Track 15
    55,  # Pink Track 16
    96,  # Green Track 17
    97,  # Green Track 18
    98,  # Green Track 19
    99,  # Green Track 20
    92,  # Green Track 21
    93,  # Green Track 22
    94,  # Green Track 23
    95,  # Green Track 24
    88,  # Green Track 25
    89,  # Green Track 26
    90,  # Green Track 27
    91,  # Green Track 28
    84,  # Green Track 29
    85,  # Green Track 30
    86,  # Green Track 31
    87,  # Green Track 32
    48,  # Yellow Track 33
    49,  # Yellow Track 34
    50,  # Yellow Track 35
    51,  # Yellow Track 36
    44,  # Yellow Track 37
    45,  # Yellow Track 38
    46,  # Yellow Track 39
    47,  # Yellow Track 40
    40,  # Yellow Track 41
    41,  # Yellow Track 42
    42,  # Yellow Track 43
    43,  # Yellow Track 44
    36,  # Yellow Track 45
    37,  # Yellow Track 46
    38,  # Yellow Track 47
    39,  # Yellow Track 48
    80,  # Blue Track 49
    81,  # Blue Track 50
    82,  # Blue Track 51
    83,  # Blue Track 52
    76,  # Blue Track 53
    77,  # Blue Track 54
    78,  # Blue Track 55
    79,  # Blue Track 56
    72,  # Blue Track 57
    73,  # Blue Track 58
    74,  # Blue Track 59
    75,  # Blue Track 60
    68,  # Blue Track 61
    69,  # Blue Track 62
    70,  # Blue Track 63
    71,  # Blue Track 64
)

TRACKMUTE = (
    -1,  # Pink Track 1
    -1,  # Pink Track 2
    -1,  # Pink Track 3
    -1,  # Pink Track 4
    -1,  # Pink Track 5
    -1,  # Pink Track 6
    -1,  # Pink Track 7
    -1,  # Pink Track 8
    -1,  # Pink Track 9
    -1,  # Pink Track 10
    -1,  # Pink Track 11
    -1,  # Pink Track 12
    -1,  # Pink Track 13
    -1,  # Pink Track 14
    -1,  # Pink Track 15
    -1,  # Pink Track 16
    -1,  # Green Track 17
    -1,  # Green Track 18
    -1,  # Green Track 19
    -1,  # Green Track 20
    -1,  # Green Track 21
    -1,  # Green Track 22
    -1,  # Green Track 23
    -1,  # Green Track 24
    -1,  # Green Track 25
    -1,  # Green Track 26
    -1,  # Green Track 27
    -1,  # Green Track 28
    -1,  # Green Track 29
    -1,  # Green Track 30
    -1,  # Green Track 31
    -1,  # Green Track 32
    -1,  # Yellow Track 33
    -1,  # Yellow Track 34
    -1,  # Yellow Track 35
    -1,  # Yellow Track 36
    -1,  # Yellow Track 37
    -1,  # Yellow Track 38
    -1,  # Yellow Track 39
    -1,  # Yellow Track 40
    -1,  # Yellow Track 41
    -1,  # Yellow Track 42
    -1,  # Yellow Track 43
    -1,  # Yellow Track 44
    -1,  # Yellow Track 45
    -1,  # Yellow Track 46
    -1,  # Yellow Track 47
    -1,  # Yellow Track 48
    -1,  # Blue Track 49
    -1,  # Blue Track 50
    -1,  # Blue Track 51
    -1,  # Blue Track 52
    -1,  # Blue Track 53
    -1,  # Blue Track 54
    -1,  # Blue Track 55
    -1,  # Blue Track 56
    -1,  # Blue Track 57
    -1,  # Blue Track 58
    -1,  # Blue Track 59
    -1,  # Blue Track 60
    -1,  # Blue Track 61
    -1,  # Blue Track 62
    -1,  # Blue Track 63
    -1,  # Blue Track 64
)

TRACKSOLO = (
    -1,  # Pink Track 1
    -1,  # Pink Track 2
    -1,  # Pink Track 3
    -1,  # Pink Track 4
    -1,  # Pink Track 5
    -1,  # Pink Track 6
    -1,  # Pink Track 7
    -1,  # Pink Track 8
    -1,  # Pink Track 9
    -1,  # Pink Track 10
    -1,  # Pink Track 11
    -1,  # Pink Track 12
    -1,  # Pink Track 13
    -1,  # Pink Track 14
    -1,  # Pink Track 15
    -1,  # Pink Track 16
    -1,  # Green Track 17
    -1,  # Green Track 18
    -1,  # Green Track 19
    -1,  # Green Track 20
    -1,  # Green Track 21
    -1,  # Green Track 22
    -1,  # Green Track 23
    -1,  # Green Track 24
    -1,  # Green Track 25
    -1,  # Green Track 26
    -1,  # Green Track 27
    -1,  # Green Track 28
    -1,  # Green Track 29
    -1,  # Green Track 30
    -1,  # Green Track 31
    -1,  # Green Track 32
    -1,  # Yellow Track 33
    -1,  # Yellow Track 34
    -1,  # Yellow Track 35
    -1,  # Yellow Track 36
    -1,  # Yellow Track 37
    -1,  # Yellow Track 38
    -1,  # Yellow Track 39
    -1,  # Yellow Track 40
    -1,  # Yellow Track 41
    -1,  # Yellow Track 42
    -1,  # Yellow Track 43
    -1,  # Yellow Track 44
    -1,  # Yellow Track 45
    -1,  # Yellow Track 46
    -1,  # Yellow Track 47
    -1,  # Yellow Track 48
    -1,  # Blue Track 49
    -1,  # Blue Track 50
    -1,  # Blue Track 51
    -1,  # Blue Track 52
    -1,  # Blue Track 53
    -1,  # Blue Track 54
    -1,  # Blue Track 55
    -1,  # Blue Track 56
    -1,  # Blue Track 57
    -1,  # Blue Track 58
    -1,  # Blue Track 59
    -1,  # Blue Track 60
    -1,  # Blue Track 61
    -1,  # Blue Track 62
    -1,  # Blue Track 63
    -1,  # Blue Track 64
)

TRACKREC = (
    -1,  # Pink Track 1
    -1,  # Pink Track 2
    -1,  # Pink Track 3
    -1,  # Pink Track 4
    -1,  # Pink Track 5
    -1,  # Pink Track 6
    -1,  # Pink Track 7
    -1,  # Pink Track 8
    -1,  # Pink Track 9
    -1,  # Pink Track 10
    -1,  # Pink Track 11
    -1,  # Pink Track 12
    -1,  # Pink Track 13
    -1,  # Pink Track 14
    -1,  # Pink Track 15
    -1,  # Pink Track 16
    -1,  # Green Track 17
    -1,  # Green Track 18
    -1,  # Green Track 19
    -1,  # Green Track 20
    -1,  # Green Track 21
    -1,  # Green Track 22
    -1,  # Green Track 23
    -1,  # Green Track 24
    -1,  # Green Track 25
    -1,  # Green Track 26
    -1,  # Green Track 27
    -1,  # Green Track 28
    -1,  # Green Track 29
    -1,  # Green Track 30
    -1,  # Green Track 31
    -1,  # Green Track 32
    -1,  # Yellow Track 33
    -1,  # Yellow Track 34
    -1,  # Yellow Track 35
    -1,  # Yellow Track 36
    -1,  # Yellow Track 37
    -1,  # Yellow Track 38
    -1,  # Yellow Track 39
    -1,  # Yellow Track 40
    -1,  # Yellow Track 41
    -1,  # Yellow Track 42
    -1,  # Yellow Track 43
    -1,  # Yellow Track 44
    -1,  # Yellow Track 45
    -1,  # Yellow Track 46
    -1,  # Yellow Track 47
    -1,  # Yellow Track 48
    -1,  # Blue Track 49
    -1,  # Blue Track 50
    -1,  # Blue Track 51
    -1,  # Blue Track 52
    -1,  # Blue Track 53
    -1,  # Blue Track 54
    -1,  # Blue Track 55
    -1,  # Blue Track 56
    -1,  # Blue Track 57
    -1,  # Blue Track 58
    -1,  # Blue Track 59
    -1,  # Blue Track 60
    -1,  # Blue Track 61
    -1,  # Blue Track 62
    -1,  # Blue Track 63
    -1,  # Blue Track 64
)


# Pad Translations for Drum Rack
PADCHANNEL = 0  # MIDI channel for Drum Rack notes
DRUM_PADS = (
    -1, -1, -1, -1,  # MIDI note numbers for 4 x 4 Drum Rack
    -1, -1, -1, -1,  # Mapping will be disabled if any notes are set to -1
    -1, -1, -1, -1,  # Notes will be "swallowed" if already mapped elsewhere
    -1, -1, -1, -1,
)


# Sliders / Knobs
# ---------------
# Valid CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments will be ignored
SLIDERCHANNEL = 0  # Channel assignment for all mapped CCs; valid range is 0 to 15
TEMPO_TOP = 180.0  # Upper limit of tempo control in BPM (max is 999)
TEMPO_BOTTOM = 100.0  # Lower limit of tempo control in BPM (min is 0)

TEMPOCONTROL = -1  # Tempo control CC assignment; control range is set above
MASTERVOLUME = -1  # Master track volume
CUELEVEL = -1  # Cue level control
CROSSFADER = -1  # Crossfader control

TRACKVOL = (
    -1,  # Pink Track 1
    -1,  # Pink Track 2
    -1,  # Pink Track 3
    -1,  # Pink Track 4
    -1,  # Pink Track 5
    -1,  # Pink Track 6
    -1,  # Pink Track 7
    -1,  # Pink Track 8
    -1,  # Pink Track 9
    -1,  # Pink Track 10
    -1,  # Pink Track 11
    -1,  # Pink Track 12
    -1,  # Pink Track 13
    -1,  # Pink Track 14
    -1,  # Pink Track 15
    -1,  # Pink Track 16
    -1,  # Green Track 17
    -1,  # Green Track 18
    -1,  # Green Track 19
    -1,  # Green Track 20
    -1,  # Green Track 21
    -1,  # Green Track 22
    -1,  # Green Track 23
    -1,  # Green Track 24
    -1,  # Green Track 25
    -1,  # Green Track 26
    -1,  # Green Track 27
    -1,  # Green Track 28
    -1,  # Green Track 29
    -1,  # Green Track 30
    -1,  # Green Track 31
    -1,  # Green Track 32
    -1,  # Yellow Track 33
    -1,  # Yellow Track 34
    -1,  # Yellow Track 35
    -1,  # Yellow Track 36
    -1,  # Yellow Track 37
    -1,  # Yellow Track 38
    -1,  # Yellow Track 39
    -1,  # Yellow Track 40
    -1,  # Yellow Track 41
    -1,  # Yellow Track 42
    -1,  # Yellow Track 43
    -1,  # Yellow Track 44
    -1,  # Yellow Track 45
    -1,  # Yellow Track 46
    -1,  # Yellow Track 47
    -1,  # Yellow Track 48
    -1,  # Blue Track 49
    -1,  # Blue Track 50
    -1,  # Blue Track 51
    -1,  # Blue Track 52
    -1,  # Blue Track 53
    -1,  # Blue Track 54
    -1,  # Blue Track 55
    -1,  # Blue Track 56
    -1,  # Blue Track 57
    -1,  # Blue Track 58
    -1,  # Blue Track 59
    -1,  # Blue Track 60
    -1,  # Blue Track 61
    -1,  # Blue Track 62
    -1,  # Blue Track 63
    -1,  # Blue Track 64
)

TRACKPAN = (
    -1,  # Pink Track 1
    -1,  # Pink Track 2
    -1,  # Pink Track 3
    -1,  # Pink Track 4
    -1,  # Pink Track 5
    -1,  # Pink Track 6
    -1,  # Pink Track 7
    -1,  # Pink Track 8
    -1,  # Pink Track 9
    -1,  # Pink Track 10
    -1,  # Pink Track 11
    -1,  # Pink Track 12
    -1,  # Pink Track 13
    -1,  # Pink Track 14
    -1,  # Pink Track 15
    -1,  # Pink Track 16
    -1,  # Green Track 17
    -1,  # Green Track 18
    -1,  # Green Track 19
    -1,  # Green Track 20
    -1,  # Green Track 21
    -1,  # Green Track 22
    -1,  # Green Track 23
    -1,  # Green Track 24
    -1,  # Green Track 25
    -1,  # Green Track 26
    -1,  # Green Track 27
    -1,  # Green Track 28
    -1,  # Green Track 29
    -1,  # Green Track 30
    -1,  # Green Track 31
    -1,  # Green Track 32
    -1,  # Yellow Track 33
    -1,  # Yellow Track 34
    -1,  # Yellow Track 35
    -1,  # Yellow Track 36
    -1,  # Yellow Track 37
    -1,  # Yellow Track 38
    -1,  # Yellow Track 39
    -1,  # Yellow Track 40
    -1,  # Yellow Track 41
    -1,  # Yellow Track 42
    -1,  # Yellow Track 43
    -1,  # Yellow Track 44
    -1,  # Yellow Track 45
    -1,  # Yellow Track 46
    -1,  # Yellow Track 47
    -1,  # Yellow Track 48
    -1,  # Blue Track 49
    -1,  # Blue Track 50
    -1,  # Blue Track 51
    -1,  # Blue Track 52
    -1,  # Blue Track 53
    -1,  # Blue Track 54
    -1,  # Blue Track 55
    -1,  # Blue Track 56
    -1,  # Blue Track 57
    -1,  # Blue Track 58
    -1,  # Blue Track 59
    -1,  # Blue Track 60
    -1,  # Blue Track 61
    -1,  # Blue Track 62
    -1,  # Blue Track 63
    -1,  # Blue Track 64
)

TRACKSENDA = (
    -1,  # Pink Track 1
    -1,  # Pink Track 2
    -1,  # Pink Track 3
    -1,  # Pink Track 4
    -1,  # Pink Track 5
    -1,  # Pink Track 6
    -1,  # Pink Track 7
    -1,  # Pink Track 8
    -1,  # Pink Track 9
    -1,  # Pink Track 10
    -1,  # Pink Track 11
    -1,  # Pink Track 12
    -1,  # Pink Track 13
    -1,  # Pink Track 14
    -1,  # Pink Track 15
    -1,  # Pink Track 16
    -1,  # Green Track 17
    -1,  # Green Track 18
    -1,  # Green Track 19
    -1,  # Green Track 20
    -1,  # Green Track 21
    -1,  # Green Track 22
    -1,  # Green Track 23
    -1,  # Green Track 24
    -1,  # Green Track 25
    -1,  # Green Track 26
    -1,  # Green Track 27
    -1,  # Green Track 28
    -1,  # Green Track 29
    -1,  # Green Track 30
    -1,  # Green Track 31
    -1,  # Green Track 32
    -1,  # Yellow Track 33
    -1,  # Yellow Track 34
    -1,  # Yellow Track 35
    -1,  # Yellow Track 36
    -1,  # Yellow Track 37
    -1,  # Yellow Track 38
    -1,  # Yellow Track 39
    -1,  # Yellow Track 40
    -1,  # Yellow Track 41
    -1,  # Yellow Track 42
    -1,  # Yellow Track 43
    -1,  # Yellow Track 44
    -1,  # Yellow Track 45
    -1,  # Yellow Track 46
    -1,  # Yellow Track 47
    -1,  # Yellow Track 48
    -1,  # Blue Track 49
    -1,  # Blue Track 50
    -1,  # Blue Track 51
    -1,  # Blue Track 52
    -1,  # Blue Track 53
    -1,  # Blue Track 54
    -1,  # Blue Track 55
    -1,  # Blue Track 56
    -1,  # Blue Track 57
    -1,  # Blue Track 58
    -1,  # Blue Track 59
    -1,  # Blue Track 60
    -1,  # Blue Track 61
    -1,  # Blue Track 62
    -1,  # Blue Track 63
    -1,  # Blue Track 64
)

TRACKSENDB = (
    -1,  # Pink Track 1
    -1,  # Pink Track 2
    -1,  # Pink Track 3
    -1,  # Pink Track 4
    -1,  # Pink Track 5
    -1,  # Pink Track 6
    -1,  # Pink Track 7
    -1,  # Pink Track 8
    -1,  # Pink Track 9
    -1,  # Pink Track 10
    -1,  # Pink Track 11
    -1,  # Pink Track 12
    -1,  # Pink Track 13
    -1,  # Pink Track 14
    -1,  # Pink Track 15
    -1,  # Pink Track 16
    -1,  # Green Track 17
    -1,  # Green Track 18
    -1,  # Green Track 19
    -1,  # Green Track 20
    -1,  # Green Track 21
    -1,  # Green Track 22
    -1,  # Green Track 23
    -1,  # Green Track 24
    -1,  # Green Track 25
    -1,  # Green Track 26
    -1,  # Green Track 27
    -1,  # Green Track 28
    -1,  # Green Track 29
    -1,  # Green Track 30
    -1,  # Green Track 31
    -1,  # Green Track 32
    -1,  # Yellow Track 33
    -1,  # Yellow Track 34
    -1,  # Yellow Track 35
    -1,  # Yellow Track 36
    -1,  # Yellow Track 37
    -1,  # Yellow Track 38
    -1,  # Yellow Track 39
    -1,  # Yellow Track 40
    -1,  # Yellow Track 41
    -1,  # Yellow Track 42
    -1,  # Yellow Track 43
    -1,  # Yellow Track 44
    -1,  # Yellow Track 45
    -1,  # Yellow Track 46
    -1,  # Yellow Track 47
    -1,  # Yellow Track 48
    -1,  # Blue Track 49
    -1,  # Blue Track 50
    -1,  # Blue Track 51
    -1,  # Blue Track 52
    -1,  # Blue Track 53
    -1,  # Blue Track 54
    -1,  # Blue Track 55
    -1,  # Blue Track 56
    -1,  # Blue Track 57
    -1,  # Blue Track 58
    -1,  # Blue Track 59
    -1,  # Blue Track 60
    -1,  # Blue Track 61
    -1,  # Blue Track 62
    -1,  # Blue Track 63
    -1,  # Blue Track 64
)

TRACKSENDC = (
    -1,  # Pink Track 1
    -1,  # Pink Track 2
    -1,  # Pink Track 3
    -1,  # Pink Track 4
    -1,  # Pink Track 5
    -1,  # Pink Track 6
    -1,  # Pink Track 7
    -1,  # Pink Track 8
    -1,  # Pink Track 9
    -1,  # Pink Track 10
    -1,  # Pink Track 11
    -1,  # Pink Track 12
    -1,  # Pink Track 13
    -1,  # Pink Track 14
    -1,  # Pink Track 15
    -1,  # Pink Track 16
    -1,  # Green Track 17
    -1,  # Green Track 18
    -1,  # Green Track 19
    -1,  # Green Track 20
    -1,  # Green Track 21
    -1,  # Green Track 22
    -1,  # Green Track 23
    -1,  # Green Track 24
    -1,  # Green Track 25
    -1,  # Green Track 26
    -1,  # Green Track 27
    -1,  # Green Track 28
    -1,  # Green Track 29
    -1,  # Green Track 30
    -1,  # Green Track 31
    -1,  # Green Track 32
    -1,  # Yellow Track 33
    -1,  # Yellow Track 34
    -1,  # Yellow Track 35
    -1,  # Yellow Track 36
    -1,  # Yellow Track 37
    -1,  # Yellow Track 38
    -1,  # Yellow Track 39
    -1,  # Yellow Track 40
    -1,  # Yellow Track 41
    -1,  # Yellow Track 42
    -1,  # Yellow Track 43
    -1,  # Yellow Track 44
    -1,  # Yellow Track 45
    -1,  # Yellow Track 46
    -1,  # Yellow Track 47
    -1,  # Yellow Track 48
    -1,  # Blue Track 49
    -1,  # Blue Track 50
    -1,  # Blue Track 51
    -1,  # Blue Track 52
    -1,  # Blue Track 53
    -1,  # Blue Track 54
    -1,  # Blue Track 55
    -1,  # Blue Track 56
    -1,  # Blue Track 57
    -1,  # Blue Track 58
    -1,  # Blue Track 59
    -1,  # Blue Track 60
    -1,  # Blue Track 61
    -1,  # Blue Track 62
    -1,  # Blue Track 63
    -1,  # Blue Track 64
)

PARAMCONTROL = (
    -1,  # Pink Track 1
    -1,  # Pink Track 2
    -1,  # Pink Track 3
    -1,  # Pink Track 4
    -1,  # Pink Track 5
    -1,  # Pink Track 6
    -1,  # Pink Track 7
    -1,  # Pink Track 8
    -1,  # Pink Track 9
    -1,  # Pink Track 10
    -1,  # Pink Track 11
    -1,  # Pink Track 12
    -1,  # Pink Track 13
    -1,  # Pink Track 14
    -1,  # Pink Track 15
    -1,  # Pink Track 16
    -1,  # Green Track 17
    -1,  # Green Track 18
    -1,  # Green Track 19
    -1,  # Green Track 20
    -1,  # Green Track 21
    -1,  # Green Track 22
    -1,  # Green Track 23
    -1,  # Green Track 24
    -1,  # Green Track 25
    -1,  # Green Track 26
    -1,  # Green Track 27
    -1,  # Green Track 28
    -1,  # Green Track 29
    -1,  # Green Track 30
    -1,  # Green Track 31
    -1,  # Green Track 32
    -1,  # Yellow Track 33
    -1,  # Yellow Track 34
    -1,  # Yellow Track 35
    -1,  # Yellow Track 36
    -1,  # Yellow Track 37
    -1,  # Yellow Track 38
    -1,  # Yellow Track 39
    -1,  # Yellow Track 40
    -1,  # Yellow Track 41
    -1,  # Yellow Track 42
    -1,  # Yellow Track 43
    -1,  # Yellow Track 44
    -1,  # Yellow Track 45
    -1,  # Yellow Track 46
    -1,  # Yellow Track 47
    -1,  # Yellow Track 48
    -1,  # Blue Track 49
    -1,  # Blue Track 50
    -1,  # Blue Track 51
    -1,  # Blue Track 52
    -1,  # Blue Track 53
    -1,  # Blue Track 54
    -1,  # Blue Track 55
    -1,  # Blue Track 56
    -1,  # Blue Track 57
    -1,  # Blue Track 58
    -1,  # Blue Track 59
    -1,  # Blue Track 60
    -1,  # Blue Track 61
    -1,  # Blue Track 62
    -1,  # Blue Track 63
    -1,  # Blue Track 64
)
