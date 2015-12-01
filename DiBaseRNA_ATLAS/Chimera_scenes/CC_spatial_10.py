import cPickle, base64
try:
	from SimpleSession.versions.v45 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 4, 29530])
import chimera
from chimera import replyobj
replyobj.status('Beginning session restore...', \
    blankAfter=0)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v45 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwpOfYdxA1UJYmFsbFNjYWxlcQRLCkc/0AAAAAAAAH2HcQVVFHJpYmJvbkhpZGVzTWFpbmNoYWlucQZLCoh9h3EHVQlwb2ludFNpemVxCEsKRz/wAAAAAAAAfYdxCVUEbmFtZXEKSwpVEENDX2RpYWdvbl82My5wZGJ9cQsoVRFDQ19kaWFnb25fMTcwLnBkYnEMXXENSwBhVRBDQ19kaWFnb25fNTYucGRicQ5dcQ9LBmFVEENDX2RpYWdvbl82NC5wZGJxEF1xEUsJYVUQQ0NfZGlhZ29uXzM2LnBkYnESXXETSwVhVRBDQ19kaWFnb25fMjcucGRicRRdcRVLAmFVEUNDX2RpYWdvbl8xNzEucGRicRZdcRdLAWFVEENDX2RpYWdvbl81Ny5wZGJxGF1xGUsHYVUQQ0NfZGlhZ29uXzI4LnBkYnEaXXEbSwNhVRBDQ19kaWFnb25fMzUucGRicRxdcR1LBGF1h3EeVQ9hcm9tYXRpY0Rpc3BsYXlxH0sKiX2HcSBVBWNvbG9ycSFLCksAfXEiKEsBXXEjSwFhSwJdcSRLAmFLA11xJUsDYUsEXXEmSwRhSwVdcSdLBWFLBl1xKEsGYUsHXXEpSwdhSwhdcSpLCGFLCV1xK0sJYXWHcSxVCG9wdGlvbmFscS19cS5VCG9wZW5lZEFzcS+ISwooVTovaG9tZS9hbGV4L0Rlc2t0b3AvZGlCYXNlX2xpYkYvQ0Mvc3BhdGlhbC9DQ19kaWFnb25fNTYucGRiVQNQREJxME6JdHExfXEyKChVOy9ob21lL2FsZXgvRGVza3RvcC9kaUJhc2VfbGliRi9DQy9zcGF0aWFsL0NDX2RpYWdvbl8xNzEucGRiaDBOiXRxM11xNEsBYShVOi9ob21lL2FsZXgvRGVza3RvcC9kaUJhc2VfbGliRi9DQy9zcGF0aWFsL0NDX2RpYWdvbl8yOC5wZGJoME6JdHE1XXE2SwNhKFU6L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL0NDL3NwYXRpYWwvQ0NfZGlhZ29uXzYzLnBkYmgwTol0cTddcThLCGEoVTovaG9tZS9hbGV4L0Rlc2t0b3AvZGlCYXNlX2xpYkYvQ0Mvc3BhdGlhbC9DQ19kaWFnb25fMjcucGRiaDBOiXRxOV1xOksCYShVOi9ob21lL2FsZXgvRGVza3RvcC9kaUJhc2VfbGliRi9DQy9zcGF0aWFsL0NDX2RpYWdvbl8zNi5wZGJoME6JdHE7XXE8SwVhKFU6L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL0NDL3NwYXRpYWwvQ0NfZGlhZ29uXzM1LnBkYmgwTol0cT1dcT5LBGEoVTsvaG9tZS9hbGV4L0Rlc2t0b3AvZGlCYXNlX2xpYkYvQ0Mvc3BhdGlhbC9DQ19kaWFnb25fMTcwLnBkYmgwTol0cT9dcUBLAGEoVTovaG9tZS9hbGV4L0Rlc2t0b3AvZGlCYXNlX2xpYkYvQ0Mvc3BhdGlhbC9DQ19kaWFnb25fNTcucGRiaDBOiXRxQV1xQksHYShVOi9ob21lL2FsZXgvRGVza3RvcC9kaUJhc2VfbGliRi9DQy9zcGF0aWFsL0NDX2RpYWdvbl82NC5wZGJoME6JdHFDXXFESwlhdYeGcUVzVQpwZGJIZWFkZXJzcUZdcUcofXFIfXFJfXFKfXFLfXFMfXFNfXFOfXFPfXFQfXFRZVUMYXJvbWF0aWNNb2RlcVJLCksBfYdxU1UDaWRzcVRLCksJSwCGfXFVKEsASwCGcVZdcVdLAGFLB0sAhnFYXXFZSwdhSwNLAIZxWl1xW0sDYUsISwCGcVxdcV1LCGFLBksAhnFeXXFfSwZhSwJLAIZxYF1xYUsCYUsFSwCGcWJdcWNLBWFLAUsAhnFkXXFlSwFhSwRLAIZxZl1xZ0sEYXWHcWhVDnN1cmZhY2VPcGFjaXR5cWlLCke/8AAAAAAAAH2HcWpVCWF1dG9jaGFpbnFrSwqIfYdxbFUKdmR3RGVuc2l0eXFtSwpHQBQAAAAAAAB9h3FuVQ1hcm9tYXRpY0NvbG9ycW9LCk59h3FwVQZoaWRkZW5xcUsKiX2HcXJVCWxpbmVXaWR0aHFzSwpHP/AAAAAAAAB9h3F0VQpzdGlja1NjYWxlcXVLCkc/8AAAAAAAAH2HcXZVB2Rpc3BsYXlxd0sKiH2HcXhVEGFyb21hdGljTGluZVR5cGVxeUsKSwJ9h3F6dS4='))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksUVQEgfYdxA1ULZmlsbERpc3BsYXlxBEsUiX2HcQVVBG5hbWVxBksUVQFDfYdxB1UFY2hhaW5xCEsUVQFBfXEJVQFCTl1xCihLAUsBhnELSwNLAYZxDEsFSwGGcQ1LB0sBhnEOSwlLAYZxD0sLSwGGcRBLDUsBhnERSw9LAYZxEksRSwGGcRNLE0sBhnEUZYZxFXOHcRZVDnJpYmJvbkRyYXdNb2RlcRdLFEsCfYdxGFUCc3NxGUsUiYmJh32HcRpVCG1vbGVjdWxlcRtLFEsAfXEcKEsBTl1xHUsCSwKGcR5hhnEfSwJOXXEgSwRLAoZxIWGGcSJLA05dcSNLBksChnEkYYZxJUsETl1xJksISwKGcSdhhnEoSwVOXXEpSwpLAoZxKmGGcStLBk5dcSxLDEsChnEtYYZxLksHTl1xL0sOSwKGcTBhhnExSwhOXXEySxBLAoZxM2GGcTRLCU5dcTVLEksChnE2YYZxN3WHcThVC3JpYmJvbkNvbG9ycTlLFE59h3E6VQVsYWJlbHE7SxRVAH2HcTxVCmxhYmVsQ29sb3JxPUsUTn2HcT5VCGZpbGxNb2RlcT9LFEsBfYdxQFUFaXNIZXRxQUsUiX2HcUJVC2xhYmVsT2Zmc2V0cUNLFE59h3FEVQhwb3NpdGlvbnFFXXFGKEsBSwKGcUdLAUsChnFISwFLAoZxSUsBSwKGcUpLAUsChnFLSwFLAoZxTEsBSwKGcU1LAUsChnFOSwFLAoZxT0sBSwKGcVBlVQ1yaWJib25EaXNwbGF5cVFLFIl9h3FSVQhvcHRpb25hbHFTfXFUVQRzc0lkcVVLFEr/////fYdxVnUu'))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVhdG9tc3ECXXEDKF1xBChLH0seZV1xBShLH0sgZV1xBihLIUsgZV1xByhLIUsiZV1xCChLIksjZV1xCShLI0skZV1xCihLI0seZV1xCyhLIkslZV1xDChLIUsmZV1xDShLJ0smZV1xDihLKEsmZV1xDyhLH0spZV1xEChLKkseZV1xEShLLEsrZV1xEihLLUsrZV1xEyhLLUsuZV1xFChLL0suZV1xFShLL0swZV1xFihLMEsxZV1xFyhLMEsyZV1xGChLMksrZV1xGShLMkszZV1xGihLL0s0ZV1xGyhLNUs0ZV1xHChLNks0ZV1xHShLLUs3ZV1xHihLOUs4ZV1xHyhLOks4ZV1xIChLO0s6ZV1xIShLO0s8ZV1xIihLPUs7ZV1xIyhLPUs+ZV1xJChLP0s+ZV1xJShLP0s4ZV1xJihLP0tAZV1xJyhLPUtBZV1xKChLQktBZV1xKShLQ0tBZV1xKihLOktEZV1xKyhLRktFZV1xLChLR0tFZV1xLShLR0tIZV1xLihLSUtHZV1xLyhLSUtKZV1xMChLS0tJZV1xMShLS0tMZV1xMihLTUtMZV1xMyhLTUtOZV1xNChLTUtFZV1xNShLS0tPZV1xNihLUEtPZV1xNyhLUUtPZV1xOChLU0tSZV1xOShLU0tUZV1xOihLVUtTZV1xOyhLVUtWZV1xPChLV0tVZV1xPShLV0tYZV1xPihLWUtYZV1xPyhLWktYZV1xQChLV0tbZV1xQShLXEtbZV1xQihLXEtSZV1xQyhLXEtdZV1xRChLXktSZV1xRShLYEtfZV1xRihLYUtfZV1xRyhLYkthZV1xSChLY0tiZV1xSShLY0tkZV1xSihLZUtkZV1xSyhLZUtmZV1xTChLZUtfZV1xTShLY0tnZV1xTihLaEtnZV1xTyhLaUtnZV1xUChLYktqZV1xUShLYUtrZV1xUihLbUtsZV1xUyhLbktsZV1xVChLbktvZV1xVShLcEtuZV1xVihLcEtxZV1xVyhLcktwZV1xWChLcktzZV1xWShLdEtzZV1xWihLdUtzZV1xWyhLckt2ZV1xXChLd0t2ZV1xXShLd0tsZV1xXihLd0t4ZV1xXyhLekt5ZV1xYChLe0t5ZV1xYShLe0t8ZV1xYihLfUt7ZV1xYyhLfkt9ZV1xZChLfkt/ZV1xZShLgEt/ZV1xZihLgEuBZV1xZyhLgEt5ZV1xaChLfkuCZV1xaShLg0uCZV1xaihLhEuCZV1xayhLfUuFZV1xbChLh0uGZV1xbShLh0uIZV1xbihLh0uJZV1xbyhLikuJZV1xcChLikuLZV1xcShLi0uMZV1xcihLi0uNZV1xcyhLjUuGZV1xdChLjUuOZV1xdShLikuPZV1xdihLkEuPZV1xdyhLkUuPZV1xeChLkkuGZV1xeShLlEuTZV1xeihLlEuVZV1xeyhLlEuWZV1xfChLl0uWZV1xfShLl0uYZV1xfihLmUuYZV1xfyhLmkuYZV1xgChLl0ubZV1xgShLm0ucZV1xgihLm0udZV1xgyhLnUuTZV1xhChLnUueZV1xhShLn0uTZV1xhihLoUugZV1xhyhLoUuiZV1xiChLoUujZV1xiShLpEujZV1xiihLpEulZV1xiyhLpUumZV1xjChLpUunZV1xjShLp0uoZV1xjihLp0ugZV1xjyhLpEupZV1xkChLqkupZV1xkShLq0upZV1xkihLrEugZV1xkyhLrkutZV1xlChLrkuvZV1xlShLrkuwZV1xlihLsUuwZV1xlyhLsUuyZV1xmChLs0uyZV1xmShLtEuyZV1xmihLsUu1ZV1xmyhLtUu2ZV1xnChLtku3ZV1xnShLtkutZV1xnihLtUu4ZV1xnyhLuUutZV1xoChLu0u6ZV1xoShLu0u8ZV1xoihLvUu7ZV1xoyhLvUu+ZV1xpChLv0u9ZV1xpShLv0vAZV1xpihLwUvAZV1xpyhLwkvAZV1xqChLv0vDZV1xqShLxEvDZV1xqihLxEu6ZV1xqyhLxEvFZV1xrChLxku6ZV1xrShLyEvHZV1xrihLyEvJZV1xryhLyEvKZV1xsChLy0vKZV1xsShLy0vMZV1xsihLzEvNZV1xsyhLzEvOZV1xtChLzkvHZV1xtShLzkvPZV1xtihLy0vQZV1xtyhL0UvQZV1xuChL0kvQZV1xuShL00vHZV1xuihL1UvUZV1xuyhL1kvUZV1xvChL1kvXZV1xvShL2EvXZV1xvihL2EvZZV1xvyhL2UvaZV1xwChL2UvbZV1xwShL20vUZV1xwihL20vcZV1xwyhL2EvdZV1xxChL3kvdZV1xxShL30vdZV1xxihL1kvgZV1xxyhL4kvhZV1xyChL40vhZV1xyShL40vkZV1xyihL5UvjZV1xyyhL5kvlZV1xzChL5kvnZV1xzShL6EvnZV1xzihL6EvhZV1xzyhL6EvpZV1x0ChL5kvqZV1x0ShL60vqZV1x0ihL7EvqZV1x0yhL5UvtZV1x1ChL70vuZV1x1ShL8EvuZV1x1ihL8EvxZV1x1yhL8kvxZV1x2ChL8kvzZV1x2ShL80v0ZV1x2ihL80v1ZV1x2yhL9Uv2ZV1x3ChL9UvuZV1x3ShL8kv3ZV1x3ihL+Ev3ZV1x3yhL+Uv3ZV1x4ChL8Ev6ZV1x4ShL/Ev7ZV1x4ihL/Uv7ZV1x4yhL/Uv+ZV1x5ChL/0v9ZV1x5ShL/00AAWVdceYoTQEBS/9lXXHnKE0BAU0CAWVdcegoTQMBTQIBZV1x6ShNBAFNAgFlXXHqKE0BAU0FAWVdcesoTQYBTQUBZV1x7ChNBgFL+2Vdce0oTQYBTQcBZV1x7ihNCQFNCAFlXXHvKE0JAU0KAWVdcfAoTQsBTQoBZV1x8ShNCwFNDAFlXXHyKE0MAU0NAWVdcfMoTQwBTQ4BZV1x9ChNDgFNCAFlXXH1KE0OAU0PAWVdcfYoTQsBTRABZV1x9yhNEQFNEAFlXXH4KE0SAU0QAWVdcfkoTQkBTRMBZV1x+ihNFAFNCAFlXXH7KE0WAU0VAWVdcfwoTRcBTRUBZV1x/ShNFwFNGAFlXXH+KE0ZAU0XAWVdcf8oTRoBTRkBZV1yAAEAAChNGgFNGwFlXXIBAQAAKE0cAU0bAWVdcgIBAAAoTR0BTRsBZV1yAwEAAChNGgFNHgFlXXIEAQAAKE0fAU0eAWVdcgUBAAAoTR8BTRUBZV1yBgEAAChNHwFNIAFlXXIHAQAAKE0ZAU0hAWVlVQVsYWJlbHIIAQAATQQBVQB9h3IJAQAAVQZyYWRpdXNyCgEAAE0EAUc/yZmZoAAAAH2HcgsBAABVC2xhYmVsT2Zmc2V0cgwBAABNBAFOfYdyDQEAAFUIZHJhd01vZGVyDgEAAE0EAUsBfYdyDwEAAFUIb3B0aW9uYWxyEAEAAH1yEQEAAFUHZGlzcGxheXISAQAATQQBSwJ9h3ITAQAAdS4='))
	crdInfo = cPickle.loads(base64.b64decode('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'))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'oneTransparentLayer': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {'Ru': ((0.141176, 0.560784, 0.560784), 1, 'default'), 'Ni': ((0.313725, 0.815686, 0.313725), 1, 'default'), 'Re': ((0.14902, 0.490196, 0.670588), 1, 'default'), 'Rf': ((0.8, 0, 0.34902), 1, 'default'), 'Ra': ((0, 0.490196, 0), 1, 'default'), 'Rb': ((0.439216, 0.180392, 0.690196), 1, 'default'), 'Rn': ((0.258824, 0.509804, 0.588235), 1, 'default'), 'Rh': ((0.0392157, 0.490196, 0.54902), 1, 'default'), 'Be': ((0.760784, 1, 0), 1, 'default'), 'Ba': ((0, 0.788235, 0), 1, 'default'), 'Bh': ((0.878431, 0, 0.219608), 1, 'default'), 'Bi': ((0.619608, 0.309804, 0.709804), 1, 'default'), 'Bk': ((0.541176, 0.309804, 0.890196), 1, 'default'), 'Br': ((0.65098, 0.160784, 0.160784), 1, 'default'), '_openColor00': ((1, 1, 1), 1, 'default'), '_openColor01': ((1, 0, 1), 1, 'default'), '_openColor02': ((0, 1, 1), 1, 'default'), '_openColor03': ((1, 1, 0), 1, 'default'), '_openColor04': ((1, 0, 0), 1, 'default'), '_openColor05': ((0, 0, 1), 1, 'default'), '_openColor06': ((0.67, 1, 0), 1, 'default'), '_openColor07': ((0.67, 0, 1), 1, 'default'), '_openColor08': ((0.67, 1, 1), 1, 'default'),
'H': ((1, 1, 1), 1, 'default'), 'P': ((1, 0.501961, 0), 1, 'default'), 'Os': ((0.14902, 0.4, 0.588235), 1, 'default'), 'Ge': ((0.4, 0.560784, 0.560784), 1, 'default'), 'Gd': ((0.270588, 1, 0.780392), 1, 'default'), 'Ga': ((0.760784, 0.560784, 0.560784), 1, 'default'), 'Pr': ((0.85098, 1, 0.780392), 1, 'default'), '_openColor12': ((1, 1, 0.5), 1, 'default'), '_openColor11': ((1, 0.67, 1), 1, 'default'), '_openColor10': ((0, 0.67, 1), 1, 'default'), 'Pt': ((0.815686, 0.815686, 0.878431), 1, 'default'), 'Pu': ((0, 0.419608, 1), 1, 'default'), 'C': ((0.564706, 0.564706, 0.564706), 1, 'default'), 'Pb': ((0.341176, 0.34902, 0.380392), 1, 'default'), 'Pa': ((0, 0.631373, 1), 1, 'default'), 'Pd': ((0, 0.411765, 0.521569), 1, 'default'), 'Xe': ((0.258824, 0.619608, 0.690196), 1, 'default'), 'Po': ((0.670588, 0.360784, 0), 1, 'default'), 'Pm': ((0.639216, 1, 0.780392), 1, 'default'), 'Hs': ((0.901961, 0, 0.180392), 1, 'default'), 'Ho': ((0, 1, 0.611765), 1, 'default'), 'Hf': ((0.301961, 0.760784, 1), 1, 'default'), 'Hg': ((0.721569, 0.721569, 0.815686), 1, 'default'),
'He': ((0.85098, 1, 1), 1, 'default'), 'Md': ((0.701961, 0.0509804, 0.65098), 1, 'default'), 'Mg': ((0.541176, 1, 0), 1, 'default'), 'K': ((0.560784, 0.25098, 0.831373), 1, 'default'), 'Mn': ((0.611765, 0.478431, 0.780392), 1, 'default'), 'O': ((1, 0.0509804, 0.0509804), 1, 'default'), 'Mt': ((0.921569, 0, 0.14902), 1, 'default'), 'S': ((1, 1, 0.188235), 1, 'default'), 'W': ((0.129412, 0.580392, 0.839216), 1, 'default'), 'Zn': ((0.490196, 0.501961, 0.690196), 1, 'default'), 'Eu': ((0.380392, 1, 0.780392), 1, 'default'), 'Zr': ((0.580392, 0.878431, 0.878431), 1, 'default'), 'Er': ((0, 0.901961, 0.458824), 1, 'default'), '_openColor13': ((1, 0, 0.5), 1, 'default'), 'No': ((0.741176, 0.0509804, 0.529412), 1, 'default'), 'Na': ((0.670588, 0.360784, 0.94902), 1, 'default'), 'Nb': ((0.45098, 0.760784, 0.788235), 1, 'default'), 'Nd': ((0.780392, 1, 0.780392), 1, 'default'), 'Ne': ((0.701961, 0.890196, 0.960784), 1, 'default'), 'Np': ((0, 0.501961, 1), 1, 'default'), 'Fr': ((0.258824, 0, 0.4), 1, 'default'), '_openColor15': ((0.67, 0.67, 1), 1, 'default'), '_openColor14': ((0, 1, 0.5), 1, 'default'),
'Fe': ((0.878431, 0.4, 0.2), 1, 'default'), 'Fm': ((0.701961, 0.121569, 0.729412), 1, 'default'), 'B': ((1, 0.709804, 0.709804), 1, 'default'), 'F': ((0.564706, 0.878431, 0.313725), 1, 'default'), 'Sr': ((0, 1, 0), 1, 'default'), 'N': ((0.188235, 0.313725, 0.972549), 1, 'default'), 'Kr': ((0.360784, 0.721569, 0.819608), 1, 'default'), 'Si': ((0.941176, 0.784314, 0.627451), 1, 'default'), 'Sn': ((0.4, 0.501961, 0.501961), 1, 'default'), 'Sm': ((0.560784, 1, 0.780392), 1, 'default'), 'V': ((0.65098, 0.65098, 0.670588), 1, 'default'), 'Sc': ((0.901961, 0.901961, 0.901961), 1, 'default'), 'Sb': ((0.619608, 0.388235, 0.709804), 1, 'default'), 'Sg': ((0.85098, 0, 0.270588), 1, 'default'), 'Se': ((1, 0.631373, 0), 1, 'default'), 'Co': ((0.941176, 0.564706, 0.627451), 1, 'default'), 'Cm': ((0.470588, 0.360784, 0.890196), 1, 'default'), 'Cl': ((0.121569, 0.941176, 0.121569), 1, 'default'), 'Ca': ((0.239216, 1, 0), 1, 'default'), 'Cf': ((0.631373, 0.211765, 0.831373), 1, 'default'), 'Ce': ((1, 1, 0.780392), 1, 'default'), 'Cd': ((1, 0.85098, 0.560784), 1, 'default'),
'Tm': ((0, 0.831373, 0.321569), 1, 'default'), 'Cs': ((0.341176, 0.0901961, 0.560784), 1, 'default'), 'Cr': ((0.541176, 0.6, 0.780392), 1, 'default'), 'Cu': ((0.784314, 0.501961, 0.2), 1, 'default'), 'La': ((0.439216, 0.831373, 1), 1, 'default'), 'Li': ((0.8, 0.501961, 1), 1, 'default'), 'Tl': ((0.65098, 0.329412, 0.301961), 1, 'default'), 'Lu': ((0, 0.670588, 0.141176), 1, 'default'), 'Lr': ((0.780392, 0, 0.4), 1, 'default'), 'Th': ((0, 0.729412, 1), 1, 'default'), 'Ti': ((0.74902, 0.760784, 0.780392), 1, 'default'), 'Te': ((0.831373, 0.478431, 0), 1, 'default'), 'Tb': ((0.188235, 1, 0.780392), 1, 'default'), 'Tc': ((0.231373, 0.619608, 0.619608), 1, 'default'), 'Ta': ((0.301961, 0.65098, 1), 1, 'default'), 'Yb': ((0, 0.74902, 0.219608), 1, 'default'), 'Db': ((0.819608, 0, 0.309804), 1, 'default'), 'Dy': ((0.121569, 1, 0.780392), 1, 'default'), '_openColor09': ((1, 0.67, 0), 1, 'default'), 'At': ((0.458824, 0.309804, 0.270588), 1, 'default'), 'I': ((0.580392, 0, 0.580392), 1, 'default'), 'U': ((0, 0.560784, 1), 1, 'default'), 'Y': ((0.580392, 1, 1), 1, 'default'),
'Ac': ((0.439216, 0.670588, 0.980392), 1, 'default'), 'Ag': ((0.752941, 0.752941, 0.752941), 1, 'default'), 'Ir': ((0.0901961, 0.329412, 0.529412), 1, 'default'), 'Am': ((0.329412, 0.360784, 0.94902), 1, 'default'), 'Al': ((0.74902, 0.65098, 0.65098), 1, 'default'), 'As': ((0.741176, 0.501961, 0.890196), 1, 'default'), 'Ar': ((0.501961, 0.819608, 0.890196), 1, 'default'), 'Au': ((1, 0.819608, 0.137255), 1, 'default'), 'Es': ((0.701961, 0.121569, 0.831373), 1, 'default'), 'In': ((0.65098, 0.458824, 0.45098), 1, 'default'), 'Mo': ((0.329412, 0.709804, 0.709804), 1, 'default')}
	materials = {'default': ((0.85, 0.85, 0.85), 30)}
	pbInfo = {'category': ['distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 13, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = {0: ('_openColor00', (1, 1, 1, 1)), 1: ('_openColor01', (1, 0, 1, 1)), 2: ('_openColor02', (0, 1, 1, 1)), 3: ('_openColor03', (1, 1, 0, 1)), 4: ('_openColor04', (1, 0, 0, 1)), 5: ('_openColor05', (0, 0, 1, 1)), 6: ('_openColor06', (0.67, 1, 0, 1)), 7: ('_openColor07', (0.67, 0, 1, 1)), 8: ('_openColor08', (0.67, 1, 1, 1)), 9: ('_openColor09', (1, 0.67, 0, 1)), 10: ('N', (0.188235, 0.313725, 0.972549, 1)), 11: ('H', (1, 1, 1, 1)), 12: ('O', (1, 0.0509804, 0.0509804, 1)), 13: ('yellow', (1, 1, 0, 1)), 14: ('white', (1, 1, 1, 1)), 15: ('green', (0, 1, 0, 1))}
	viewerInfo = {'cameraAttrs': {'center': (4.575, -2.0665, -28.5181), 'fieldOfView': 26.2751, 'nearFar': (-20.5033, -36.6244), 'ortho': False, 'eyeSeparation': 50.8, 'focal': -28.7795}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'viewSize': 1.13362, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 1, 'depthCue': True, 'highlight': 0, 'scaleFactor': 0.11365}, 'viewerHL': 15, 'cameraMode': 'mono', 'detail': 1, 'viewerFog': None, 'viewerBG': 14}

	replyobj.status("Initializing session restore...", blankAfter=0)
	init(colorInfo)
	replyobj.status("Restoring colors...", blankAfter=0)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0)


def restoreLightController():
	import Lighting
	c = Lighting.get().setFromParams({'quality': 'normal', 'shininess': (30.0, (0.84999999999999998, 0.84999999999999998, 0.84999999999999998), 1.0), 'key': (True, (1.0, 1.0, 1.0), 0.65327227115631104, (1.0, 1.0, 1.0), 1.0, (-0.35740674433659325, 0.66040155174814552, 0.66040155174814552)), 'fill': (True, (1.0, 1.0, 1.0), 0.49998998641967773, (1.0, 1.0, 1.0), 0.0, (0.25056280708573153, 0.25056280708573153, 0.9351131265310294))})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")


def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = []
	userXSections = []
	userResidueClasses = []
	residueData = [(10, 'Chimera default', 'rounded', 'unknown'), (11, 'Chimera default', 'rounded', 'unknown'), (12, 'Chimera default', 'rounded', 'unknown'), (13, 'Chimera default', 'rounded', 'unknown'), (14, 'Chimera default', 'rounded', 'unknown'), (15, 'Chimera default', 'rounded', 'unknown'), (16, 'Chimera default', 'rounded', 'unknown'), (17, 'Chimera default', 'rounded', 'unknown'), (18, 'Chimera default', 'rounded', 'unknown'), (19, 'Chimera default', 'rounded', 'unknown'), (20, 'Chimera default', 'rounded', 'unknown'), (21, 'Chimera default', 'rounded', 'unknown'), (22, 'Chimera default', 'rounded', 'unknown'), (23, 'Chimera default', 'rounded', 'unknown'), (24, 'Chimera default', 'rounded', 'unknown'), (25, 'Chimera default', 'rounded', 'unknown'), (26, 'Chimera default', 'rounded', 'unknown'), (27, 'Chimera default', 'rounded', 'unknown'), (28, 'Chimera default', 'rounded', 'unknown'), (29, 'Chimera default', 'rounded', 'unknown')]
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")
geomData = {'AxisManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')


def restoreMidasBase():
	import chimera
	from SimpleSession import modelMap, modelOffset
	def deformatPosition(pos):
		xfDict = {}
		for molId, xfData in pos[5].items():
			mid, subid = molId
			trData, rotData = xfData
			xf = chimera.Xform.translation(*trData)
			xf.rotate(*rotData)
			xfDict[(mid+modelOffset, subid)] = xf
		try:
			from chimera.misc import KludgeWeakWrappyDict
			clipDict = KludgeWeakWrappyDict("Model")
		except ImportError:
			from weakref import WeakKeyDictionary
			clipDict = WeakKeyDictionary()
		for clipID, clipInfo in pos[6].items():
			mid, subid, className = clipID
			models = [m for m in modelMap.get((mid, subid), [])
					if m.__class__.__name__ == className]
			if not models:
				continue
			useClip, ox, oy, oz, nx, ny, nz, useThick, thickness = clipInfo
			if useClip:
				origin = chimera.Point(ox, oy, oz)
				normal = chimera.Vector(nx, ny, nz)
				plane = chimera.Plane(origin, normal)
			else:
				plane = chimera.Plane()
			for m in models:
				clipDict[m] = (useClip, plane,
							useThick, thickness)
		return pos[:5] + (xfDict, clipDict) + pos[7:]
	formattedPositions = {}
	positions = {}
	for name, fpos in formattedPositions.items():
		positions[name] = deformatPosition(fpos)
	import Midas
	if modelOffset == 0:
		Midas.positions.clear()
	Midas.positions.update(positions)
	positionStack = []
	Midas._positionStack = map(deformatPosition, positionStack)

def delayedMidasBase():
	try:
		restoreMidasBase()
	except:
		reportRestoreError('Error restoring Midas base state')
import SimpleSession
SimpleSession.registerAfterModelsCB(delayedMidasBase)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreRemainder():
	from SimpleSession.versions.v45 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 4 }
	windowSize = (1270, 607)
	xformMap = {0: (((-0.941273, 0.0511255, 0.333753), 92.332), (-8.21509, 24.2451, -26.7333), True), 1: (((-0.15768, 0.933006, -0.323476), 173.312), (14.6544, -14.6617, -53.1814), True), 2: (((0.579795, -0.234033, -0.780427), 70.7294), (-0.607633, 18.8882, -38.5086), True), 3: (((0.459039, 0.155502, 0.874701), 140.724), (2.49564, -12.026, -50.0605), True), 4: (((-0.0813315, 0.894846, -0.438902), 172.244), (27.1546, 28.5911, 6.15806), True), 5: (((-0.926115, -0.0201734, 0.376701), 85.711), (-3.45413, -51.56, -16.9189), True), 6: (((0.262745, 0.494648, 0.828425), 167.901), (-14.4071, 14.0985, -44.502), True), 7: (((0.912784, 0.0122669, -0.408258), 101.636), (11.1493, -0.0553089, -57.3391), True), 8: (((-0.344282, -0.871449, 0.349352), 167.008), (7.95052, 1.69094, -27.2338), True), 9: (((-0.861282, 0.397848, 0.316085), 119.187), (2.77158, -6.78046, -28.131), True)}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}

	replyobj.status("Restoring window...", blankAfter=0)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0)
	restoreModelClip(clipPlaneInfo)

	replyobj.status("Restoring remaining extension info...", blankAfter=0)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v45 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v45 import endRestore
replyobj.status('Finishing restore...', blankAfter=0)
endRestore()
replyobj.status('Restore finished.')

