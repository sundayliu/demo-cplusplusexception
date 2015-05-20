typedef enum{
    _URC_NO_REASON = 0,
    _URC_FOREIGN_EXCEPTION_CAUGHT = 1,
	_URC_FATAL_PHASE2_ERROR = 2,
	_URC_FATAL_PHASE1_ERROR = 3,
	_URC_NORMAL_STOP = 4,
	_URC_END_OF_STACK = 5,
	_URC_HANDLER_FOUND = 6,
	_URC_INSTALL_CONTEXT = 7,
	_URC_CONTINUE_UNWIND = 8
}_Unwind_Reason_Code

typedef int _Unwind_Action;
static const _Unwind_Action _UA_SEARCH_PHASE = 1;
static const _Unwind_Action _UA_CLEANUP_PHASE = 2;
static const _Unwind_Action _UA_HANDLER_FRAME = 4;
static const _Unwind_Action _UA_FORCE_UNWIND = 8;

_Unwind_Reason_Code (* __personality_routine)(
    int version, // currently 1
    _Unwind_Action actions,
    uint64 exceptionClass,
    struct _Unwind_Exception* exceptionObject,
    struct _Unwind_Context* context
)