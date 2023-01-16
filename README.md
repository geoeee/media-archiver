# media-archiver

## Python
Version: 3.11.0

### Functions

### Workflow

#### Handle logic

```mermaid
flowchart LR
  start[Got one file]
  isTargetedFile{targeted file?}
  isAlreadyHandled{already handled?}
  handle[Handle]
  notHandle[Not handle]

  start --> isTargetedFile
  isTargetedFile --> |Y| isAlreadyHandled
  isTargetedFile --> |N| notHandle

  isAlreadyHandled --> |Y| notHandle
  isAlreadyHandled --> |N| handle

```

#### Output summary

```mermaid

flowchart LR
  out[Output Summary]
  fileTouched[File have been handled]
  fileNotTouched[FIle not handled]
  notTargetFile[Not targeted file]
  alreadyHandled[File have handled before]

  out --> fileTouched
  out --> fileNotTouched
  fileNotTouched --> notTargetFile
  fileNotTouched --> alreadyHandled


```

## References

- https://blog.csdn.net/wangli_010/article/details/127402288
- https://github.com/pallets/click
- 