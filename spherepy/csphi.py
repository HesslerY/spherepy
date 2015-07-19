# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_csphi', [dirname(__file__)])
        except ImportError:
            import _csphi
            return _csphi
        if fp is not None:
            try:
                _mod = imp.load_module('_csphi', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _csphi = swig_import_helper()
    del swig_import_helper
else:
    import _csphi
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SCOMPLEX(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SCOMPLEX, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SCOMPLEX, name)
    __repr__ = _swig_repr
    __swig_setmethods__["r"] = _csphi.SCOMPLEX_r_set
    __swig_getmethods__["r"] = _csphi.SCOMPLEX_r_get
    if _newclass:r = _swig_property(_csphi.SCOMPLEX_r_get, _csphi.SCOMPLEX_r_set)
    __swig_setmethods__["i"] = _csphi.SCOMPLEX_i_set
    __swig_getmethods__["i"] = _csphi.SCOMPLEX_i_get
    if _newclass:i = _swig_property(_csphi.SCOMPLEX_i_get, _csphi.SCOMPLEX_i_set)
    def __init__(self): 
        this = _csphi.new_SCOMPLEX()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _csphi.delete_SCOMPLEX
    __del__ = lambda self : None;
SCOMPLEX_swigregister = _csphi.SCOMPLEX_swigregister
SCOMPLEX_swigregister(SCOMPLEX)

SUCCESS = _csphi.SUCCESS
OUTBOUNDS = _csphi.OUTBOUNDS
PI = _csphi.PI

def ynnm(*args):
  return _csphi.ynnm(*args)
ynnm = _csphi.ynnm

def new_SFLOAT(*args):
  return _csphi.new_SFLOAT(*args)
new_SFLOAT = _csphi.new_SFLOAT

def new_SINT(*args):
  return _csphi.new_SINT(*args)
new_SINT = _csphi.new_SINT

def get_SFLOAT(*args):
  return _csphi.get_SFLOAT(*args)
get_SFLOAT = _csphi.get_SFLOAT

def get_SINT(*args):
  return _csphi.get_SINT(*args)
get_SINT = _csphi.get_SINT

def delete_SFLOAT(*args):
  return _csphi.delete_SFLOAT(*args)
delete_SFLOAT = _csphi.delete_SFLOAT

def delete_SINT(*args):
  return _csphi.delete_SINT(*args)
delete_SINT = _csphi.delete_SINT

def ynnm_hdr(*args):
  return _csphi.ynnm_hdr(*args)
ynnm_hdr = _csphi.ynnm_hdr

def ynunm(*args):
  return _csphi.ynunm(*args)
ynunm = _csphi.ynunm

def ynunm_hdr(*args):
  return _csphi.ynunm_hdr(*args)
ynunm_hdr = _csphi.ynunm_hdr

def FindQ(*args):
  return _csphi.FindQ(*args)
FindQ = _csphi.FindQ

def SData(*args):
  return _csphi.SData(*args)
SData = _csphi.SData

def hkm_fc(*args):
  return _csphi.hkm_fc(*args)
hkm_fc = _csphi.hkm_fc

def bnm_fc(*args):
  return _csphi.bnm_fc(*args)
bnm_fc = _csphi.bnm_fc

def bnm_fc_hdr(*args):
  return _csphi.bnm_fc_hdr(*args)
bnm_fc_hdr = _csphi.bnm_fc_hdr

def fc_to_sc(*args):
  return _csphi.fc_to_sc(*args)
fc_to_sc = _csphi.fc_to_sc

def fc_to_sc_hdr(*args):
  return _csphi.fc_to_sc_hdr(*args)
fc_to_sc_hdr = _csphi.fc_to_sc_hdr

def fcvec_m_sc(*args):
  return _csphi.fcvec_m_sc(*args)
fcvec_m_sc = _csphi.fcvec_m_sc

def fcvec_m_sc_hdr(*args):
  return _csphi.fcvec_m_sc_hdr(*args)
fcvec_m_sc_hdr = _csphi.fcvec_m_sc_hdr

def sc_to_fc(*args):
  return _csphi.sc_to_fc(*args)
sc_to_fc = _csphi.sc_to_fc

def sc_to_fc_hdr(*args):
  return _csphi.sc_to_fc_hdr(*args)
sc_to_fc_hdr = _csphi.sc_to_fc_hdr
# This file is compatible with both classic and new-style classes.


