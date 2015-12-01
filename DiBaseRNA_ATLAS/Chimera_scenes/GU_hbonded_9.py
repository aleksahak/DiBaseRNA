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
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwlOfYdxA1UJYmFsbFNjYWxlcQRLCUc/0AAAAAAAAH2HcQVVFHJpYmJvbkhpZGVzTWFpbmNoYWlucQZLCYh9h3EHVQlwb2ludFNpemVxCEsJRz/wAAAAAAAAfYdxCVUEbmFtZXEKSwlVEUdVX3BsYW5hcl8xNTYucGRifXELKFURR1VfcGxhbmFyXzE4MS5wZGJxDF1xDUsHYVURR1VfcGxhbmFyXzE4My5wZGJxDl1xD0sIYVUQR1VfcGxhbmFyXzEzLnBkYnEQXXERSwJhVRFHVV9wbGFuYXJfMTU1LnBkYnESXXETSwVhVRBHVV9kaWFnb25fODkucGRicRRdcRVLAGFVEEdVX3BsYW5hcl8xMS5wZGJxFl1xF0sBYVURR1VfcGxhbmFyXzEzNi5wZGJxGF1xGUsDYVURR1VfcGxhbmFyXzEzNy5wZGJxGl1xG0sEYXWHcRxVD2Fyb21hdGljRGlzcGxheXEdSwmJfYdxHlUFY29sb3JxH0sJSwB9cSAoSwFdcSFLAWFLAl1xIksCYUsDXXEjSwNhSwRdcSRLBGFLBV1xJUsFYUsGXXEmSwZhSwddcSdLB2FLCF1xKEsIYXWHcSlVCG9wdGlvbmFscSp9cStVCG9wZW5lZEFzcSyISwkoVTsvaG9tZS9hbGV4L0Rlc2t0b3AvZGlCYXNlX2xpYkYvR1UvaF9ib25kZWQvR1VfZGlhZ29uXzg5LnBkYlUDUERCcS1OiXRxLn1xLygoVTwvaG9tZS9hbGV4L0Rlc2t0b3AvZGlCYXNlX2xpYkYvR1UvaF9ib25kZWQvR1VfcGxhbmFyXzE1Ni5wZGJoLU6JdHEwXXExSwZhKFU8L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL0dVL2hfYm9uZGVkL0dVX3BsYW5hcl8xMzcucGRiaC1OiXRxMl1xM0sEYShVOy9ob21lL2FsZXgvRGVza3RvcC9kaUJhc2VfbGliRi9HVS9oX2JvbmRlZC9HVV9wbGFuYXJfMTEucGRiaC1OiXRxNF1xNUsBYShVPC9ob21lL2FsZXgvRGVza3RvcC9kaUJhc2VfbGliRi9HVS9oX2JvbmRlZC9HVV9wbGFuYXJfMTgzLnBkYmgtTol0cTZdcTdLCGEoVTwvaG9tZS9hbGV4L0Rlc2t0b3AvZGlCYXNlX2xpYkYvR1UvaF9ib25kZWQvR1VfcGxhbmFyXzE4MS5wZGJoLU6JdHE4XXE5SwdhKFU8L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL0dVL2hfYm9uZGVkL0dVX3BsYW5hcl8xNTUucGRiaC1OiXRxOl1xO0sFYShVOy9ob21lL2FsZXgvRGVza3RvcC9kaUJhc2VfbGliRi9HVS9oX2JvbmRlZC9HVV9wbGFuYXJfMTMucGRiaC1OiXRxPF1xPUsCYShVPC9ob21lL2FsZXgvRGVza3RvcC9kaUJhc2VfbGliRi9HVS9oX2JvbmRlZC9HVV9wbGFuYXJfMTM2LnBkYmgtTol0cT5dcT9LA2F1h4ZxQHNVCnBkYkhlYWRlcnNxQV1xQih9cUN9cUR9cUV9cUZ9cUd9cUh9cUl9cUp9cUtlVQxhcm9tYXRpY01vZGVxTEsJSwF9h3FNVQNpZHNxTksJSwBLAIZ9cU8oSwdLAIZxUF1xUUsHYUsDSwCGcVJdcVNLA2FLCEsAhnFUXXFVSwhhSwZLAIZxVl1xV0sGYUsCSwCGcVhdcVlLAmFLBUsAhnFaXXFbSwVhSwFLAIZxXF1xXUsBYUsESwCGcV5dcV9LBGF1h3FgVQ5zdXJmYWNlT3BhY2l0eXFhSwlHv/AAAAAAAAB9h3FiVQlhdXRvY2hhaW5xY0sJiH2HcWRVCnZkd0RlbnNpdHlxZUsJR0AUAAAAAAAAfYdxZlUNYXJvbWF0aWNDb2xvcnFnSwlOfYdxaFUGaGlkZGVucWlLCYl9h3FqVQlsaW5lV2lkdGhxa0sJRz/wAAAAAAAAfYdxbFUKc3RpY2tTY2FsZXFtSwlHP/AAAAAAAAB9h3FuVQdkaXNwbGF5cW9LCYh9h3FwVRBhcm9tYXRpY0xpbmVUeXBlcXFLCUsCfYdxcnUu'))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksSVQEgfYdxA1ULZmlsbERpc3BsYXlxBEsSiX2HcQVVBG5hbWVxBksSVQFVfXEHVQFHXXEIKEsASwJLBEsGSwhLCksMSw5LEGVzh3EJVQVjaGFpbnEKSxJVAUF9cQtVAUJOXXEMKEsBSwGGcQ1LA0sBhnEOSwVLAYZxD0sHSwGGcRBLCUsBhnERSwtLAYZxEksNSwGGcRNLD0sBhnEUSxFLAYZxFWWGcRZzh3EXVQ5yaWJib25EcmF3TW9kZXEYSxJLAn2HcRlVAnNzcRpLEomJiYd9h3EbVQhtb2xlY3VsZXEcSxJLAH1xHShLAU5dcR5LAksChnEfYYZxIEsCTl1xIUsESwKGcSJhhnEjSwNOXXEkSwZLAoZxJWGGcSZLBE5dcSdLCEsChnEoYYZxKUsFTl1xKksKSwKGcSthhnEsSwZOXXEtSwxLAoZxLmGGcS9LB05dcTBLDksChnExYYZxMksITl1xM0sQSwKGcTRhhnE1dYdxNlULcmliYm9uQ29sb3JxN0sSTn2HcThVBWxhYmVscTlLElUAfYdxOlUKbGFiZWxDb2xvcnE7SxJOfYdxPFUIZmlsbE1vZGVxPUsSSwF9h3E+VQVpc0hldHE/SxKJfYdxQFULbGFiZWxPZmZzZXRxQUsSTn2HcUJVCHBvc2l0aW9ucUNdcUQoSwFLAoZxRUsBSwKGcUZLAUsChnFHSwFLAoZxSEsBSwKGcUlLAUsChnFKSwFLAoZxS0sBSwKGcUxLAUsChnFNZVUNcmliYm9uRGlzcGxheXFOSxKJfYdxT1UIb3B0aW9uYWxxUH1xUVUEc3NJZHFSSxJK/////32HcVN1Lg=='))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVhdG9tc3ECXXEDKF1xBChLHEsbZV1xBShLHUsbZV1xBihLHUseZV1xByhLH0seZV1xCChLH0sgZV1xCShLIEshZV1xCihLIEsiZV1xCyhLI0siZV1xDChLJEsiZV1xDShLJEslZV1xDihLJkslZV1xDyhLJ0slZV1xEChLJEsoZV1xEShLKUsoZV1xEihLKUsbZV1xEyhLKUsfZV1xFChLHUsqZV1xFShLLEsrZV1xFihLLEstZV1xFyhLLkssZV1xGChLLksvZV1xGShLMEsuZV1xGihLMEsxZV1xGyhLMksxZV1xHChLM0sxZV1xHShLM0s0ZV1xHihLM0srZV1xHyhLMEs1ZV1xIChLNksrZV1xIShLOEs3ZV1xIihLOUs3ZV1xIyhLOUs6ZV1xJChLO0s6ZV1xJShLO0s8ZV1xJihLPEs9ZV1xJyhLPks9ZV1xKChLPks/ZV1xKShLQEs/ZV1xKihLQEs3ZV1xKyhLQEs7ZV1xLChLPktBZV1xLShLQktBZV1xLihLQ0tBZV1xLyhLREs9ZV1xMChLPEtFZV1xMShLOUtGZV1xMihLSEtHZV1xMyhLSUtHZV1xNChLSUtKZV1xNShLS0tKZV1xNihLS0tMZV1xNyhLS0tNZV1xOChLTUtOZV1xOShLTktPZV1xOihLTktHZV1xOyhLTUtQZV1xPChLUUtKZV1xPShLSUtSZV1xPihLVEtTZV1xPyhLVEtVZV1xQChLVUtWZV1xQShLV0tWZV1xQihLV0tYZV1xQyhLV0tTZV1xRChLVUtZZV1xRShLWUtaZV1xRihLWUtbZV1xRyhLXEtbZV1xSChLXEtdZV1xSShLXktdZV1xSihLX0tdZV1xSyhLXEtgZV1xTChLVEtgZV1xTShLYUtbZV1xTihLYktTZV1xTyhLZEtjZV1xUChLZUtkZV1xUShLZktlZV1xUihLZktnZV1xUyhLaEtnZV1xVChLaUtnZV1xVShLaUtjZV1xVihLaUtqZV1xVyhLZktrZV1xWChLZUtsZV1xWShLZEttZV1xWihLbktjZV1xWyhLcEtvZV1xXChLcEtxZV1xXShLcUtyZV1xXihLc0tyZV1xXyhLc0tvZV1xYChLc0t0ZV1xYShLcUt1ZV1xYihLdUt2ZV1xYyhLd0t2ZV1xZChLd0t4ZV1xZShLcEt4ZV1xZihLd0t5ZV1xZyhLekt5ZV1xaChLe0t5ZV1xaShLfEt2ZV1xaihLdUt9ZV1xayhLfktvZV1xbChLgEt/ZV1xbShLgUt/ZV1xbihLgUuCZV1xbyhLg0uCZV1xcChLhEuCZV1xcShLhEuFZV1xcihLhUuGZV1xcyhLhUuHZV1xdChLh0uIZV1xdShLh0t/ZV1xdihLhEuJZV1xdyhLgUuKZV1xeChLjEuLZV1xeShLjEuNZV1xeihLjUuOZV1xeyhLjkuPZV1xfChLkEuPZV1xfShLkUuPZV1xfihLkUuSZV1xfyhLk0uSZV1xgChLlEuSZV1xgShLkUuVZV1xgihLjEuVZV1xgyhLjkuWZV1xhChLjUuXZV1xhShLmEuXZV1xhihLmEuLZV1xhyhLmEuZZV1xiChLmkuLZV1xiShLnEubZV1xiihLnEudZV1xiyhLnkucZV1xjChLnkufZV1xjShLoEueZV1xjihLoEuhZV1xjyhLoEuiZV1xkChLo0uiZV1xkShLo0ubZV1xkihLo0ukZV1xkyhLpUuiZV1xlChLpkubZV1xlShLqEunZV1xlihLqEupZV1xlyhLqkupZV1xmChLqkurZV1xmShLq0usZV1xmihLrUusZV1xmyhLrkusZV1xnChLrkuvZV1xnShLsEuvZV1xnihLsEuqZV1xnyhLsEunZV1xoChLrkuxZV1xoShLskuxZV1xoihLs0uxZV1xoyhLq0u0ZV1xpChLqEu1ZV1xpShLtkunZV1xpihLuEu3ZV1xpyhLuUu3ZV1xqChLuUu6ZV1xqShLuUu7ZV1xqihLvEu7ZV1xqyhLvUu7ZV1xrChLvUu+ZV1xrShLvku/ZV1xrihLvkvAZV1xryhLwEvBZV1xsChLwEu3ZV1xsShLvUvCZV1xsihLxEvDZV1xsyhLxUvDZV1xtChLxUvGZV1xtShLxUvHZV1xtihLyEvHZV1xtyhLyEvJZV1xuChLyUvKZV1xuShLyUvLZV1xuihLzEvLZV1xuyhLzEvNZV1xvChLzkvNZV1xvShLz0vNZV1xvihLzEvQZV1xvyhL0UvQZV1xwChL0UvDZV1xwShL0UvIZV1xwihL0kvLZV1xwyhL1EvTZV1xxChL1EvVZV1xxShL1kvUZV1xxihL1kvXZV1xxyhL2EvWZV1xyChL2EvZZV1xyShL2kvZZV1xyihL20vZZV1xyyhL20vTZV1xzChL20vcZV1xzShL2EvdZV1xzihL3kvTZV1xzyhL4EvfZV1x0ChL4EvhZV1x0ShL4EviZV1x0ihL40viZV1x0yhL40vkZV1x1ChL5EvlZV1x1ShL5kvlZV1x1ihL5kvnZV1x1yhL6EvnZV1x2ChL6EvjZV1x2ShL6EvfZV1x2ihL5kvpZV1x2yhL6kvpZV1x3ChL60vpZV1x3ShL7EvlZV1x3ihL5EvtZV1x3yhL7kvfZV1x4ChL8EvvZV1x4ShL8UvvZV1x4ihL8UvyZV1x4yhL80vyZV1x5ChL9EvyZV1x5ShL9Ev1ZV1x5ihL9Ev2ZV1x5yhL9kv3ZV1x6ChL9kv4ZV1x6ShL+EvvZV1x6ihL+Ev5ZV1x6yhL8Uv6ZV1x7ChL/Ev7ZV1x7ShL/Uv7ZV1x7ihL/Uv+ZV1x7yhL/Uv/ZV1x8ChNAAFL/2VdcfEoTQABTQEBZV1x8ihNAQFNAgFlXXHzKE0DAU0CAWVdcfQoTQMBTQQBZV1x9ShNBQFNBAFlXXH2KE0GAU0EAWVdcfcoTQMBTQcBZV1x+ChNCAFNBwFlXXH5KE0IAUv7ZV1x+ihNCAFNAAFlXXH7KE0JAU0CAWVdcfwoTQEBTQoBZV1x/ShNDAFNCwFlXXH+KE0NAU0LAWVdcf8oTQ4BTQ0BZV1yAAEAAChNDwFNDgFlXXIBAQAAKE0PAU0QAWVdcgIBAAAoTQ8BTREBZV1yAwEAAChNEgFNEQFlXXIEAQAAKE0SAU0LAWVdcgUBAAAoTRIBTRMBZV1yBgEAAChNFAFNEQFlXXIHAQAAKE0OAU0VAWVdcggBAAAoTQ0BTRYBZWVVBWxhYmVscgkBAABNBQFVAH2HcgoBAABVBnJhZGl1c3ILAQAATQUBRz/JmZmgAAAAfYdyDAEAAFULbGFiZWxPZmZzZXRyDQEAAE0FAU59h3IOAQAAVQhkcmF3TW9kZXIPAQAATQUBSwF9h3IQAQAAVQhvcHRpb25hbHIRAQAAfXISAQAAVQdkaXNwbGF5chMBAABNBQFLAn2HchQBAAB1Lg=='))
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
	pbInfo = {'category': ['distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 12, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = {0: ('_openColor00', (1, 1, 1, 1)), 1: ('_openColor01', (1, 0, 1, 1)), 2: ('_openColor02', (0, 1, 1, 1)), 3: ('_openColor03', (1, 1, 0, 1)), 4: ('_openColor04', (1, 0, 0, 1)), 5: ('_openColor05', (0, 0, 1, 1)), 6: ('_openColor06', (0.67, 1, 0, 1)), 7: ('_openColor07', (0.67, 0, 1, 1)), 8: ('_openColor08', (0.67, 1, 1, 1)), 9: ('N', (0.188235, 0.313725, 0.972549, 1)), 10: ('H', (1, 1, 1, 1)), 11: ('O', (1, 0.0509804, 0.0509804, 1)), 12: ('yellow', (1, 1, 0, 1)), 13: ('white', (1, 1, 1, 1)), 14: ('green', (0, 1, 0, 1))}
	viewerInfo = {'cameraAttrs': {'center': (11.1575, 29.1535, 7.11289), 'fieldOfView': 26.2751, 'nearFar': (15.6726, -1.44678), 'ortho': False, 'eyeSeparation': 50.8, 'focal': -10.602}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'viewSize': 8.01894, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 1, 'depthCue': True, 'highlight': 0, 'scaleFactor': 0.552622}, 'viewerHL': 14, 'cameraMode': 'mono', 'detail': 1, 'viewerFog': None, 'viewerBG': 13}

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
	residueData = [(9, 'Chimera default', 'rounded', 'unknown'), (10, 'Chimera default', 'rounded', 'unknown'), (11, 'Chimera default', 'rounded', 'unknown'), (12, 'Chimera default', 'rounded', 'unknown'), (13, 'Chimera default', 'rounded', 'unknown'), (14, 'Chimera default', 'rounded', 'unknown'), (15, 'Chimera default', 'rounded', 'unknown'), (16, 'Chimera default', 'rounded', 'unknown'), (17, 'Chimera default', 'rounded', 'unknown'), (18, 'Chimera default', 'rounded', 'unknown'), (19, 'Chimera default', 'rounded', 'unknown'), (20, 'Chimera default', 'rounded', 'unknown'), (21, 'Chimera default', 'rounded', 'unknown'), (22, 'Chimera default', 'rounded', 'unknown'), (23, 'Chimera default', 'rounded', 'unknown'), (24, 'Chimera default', 'rounded', 'unknown'), (25, 'Chimera default', 'rounded', 'unknown'), (26, 'Chimera default', 'rounded', 'unknown')]
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
	xformMap = {0: (((-0.574979, 0.806108, -0.139963), 158.121), (43.5323, 29.8513, 12.4642), True), 1: (((0.503169, 0.82602, -0.253993), 142.469), (-16.6173, 31.7013, 47.4666), True), 2: (((-0.473733, 0.170016, 0.864102), 95.8004), (38.7117, -10.7731, -1.0397), True), 3: (((0.732379, 0.446219, -0.514304), 122.321), (-23.4184, 43.0152, 17.4626), True), 4: (((0.144801, 0.126939, 0.981284), 111.506), (38.6062, 20.5412, -15.0566), True), 5: (((-0.466583, -0.808915, -0.35771), 116.96), (22.532, 0.0159838, -33.5734), True), 6: (((-0.507146, -0.630897, -0.587173), 140.418), (16.2984, -1.34, -37.6463), True), 7: (((0.773813, 0.404622, -0.487334), 124.002), (-15.2912, 58.5297, 23.8408), True), 8: (((0.140274, 0.196012, 0.970517), 125.865), (30.7407, 17.4855, -30.5469), True)}
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

