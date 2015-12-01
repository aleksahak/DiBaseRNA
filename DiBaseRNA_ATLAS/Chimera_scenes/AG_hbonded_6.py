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
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwZOfYdxA1UJYmFsbFNjYWxlcQRLBkc/0AAAAAAAAH2HcQVVFHJpYmJvbkhpZGVzTWFpbmNoYWlucQZLBoh9h3EHVQlwb2ludFNpemVxCEsGRz/wAAAAAAAAfYdxCVUEbmFtZXEKSwZVEUFHX3BsYW5hcl8xMDAucGRifXELKFUQQUdfcGxhbmFyXzc5LnBkYnEMXXENSwRhVRFBR19wbGFuYXJfMTM4LnBkYnEOXXEPSwJhVRBBR19wbGFuYXJfNDcucGRicRBdcRFLA2FVEUFHX2RpYWdvbl8xMTQucGRicRJdcRNLAGFVEEFHX3BsYW5hcl85OS5wZGJxFF1xFUsFYXWHcRZVD2Fyb21hdGljRGlzcGxheXEXSwaJfYdxGFUFY29sb3JxGUsGSwB9cRooSwFdcRtLAWFLAl1xHEsCYUsDXXEdSwNhSwRdcR5LBGFLBV1xH0sFYXWHcSBVCG9wdGlvbmFscSF9cSJVCG9wZW5lZEFzcSOISwYoVTsvaG9tZS9hbGV4L0Rlc2t0b3AvZGlCYXNlX2xpYkYvQUcvaF9ib25kZWQvQUdfcGxhbmFyXzc5LnBkYlUDUERCcSROiXRxJX1xJigoVTsvaG9tZS9hbGV4L0Rlc2t0b3AvZGlCYXNlX2xpYkYvQUcvaF9ib25kZWQvQUdfcGxhbmFyXzQ3LnBkYmgkTol0cSddcShLA2EoVTwvaG9tZS9hbGV4L0Rlc2t0b3AvZGlCYXNlX2xpYkYvQUcvaF9ib25kZWQvQUdfcGxhbmFyXzEwMC5wZGJoJE6JdHEpXXEqSwFhKFU7L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL0FHL2hfYm9uZGVkL0FHX3BsYW5hcl85OS5wZGJoJE6JdHErXXEsSwVhKFU8L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL0FHL2hfYm9uZGVkL0FHX2RpYWdvbl8xMTQucGRiaCROiXRxLV1xLksAYShVPC9ob21lL2FsZXgvRGVza3RvcC9kaUJhc2VfbGliRi9BRy9oX2JvbmRlZC9BR19wbGFuYXJfMTM4LnBkYmgkTol0cS9dcTBLAmF1h4ZxMXNVCnBkYkhlYWRlcnNxMl1xMyh9cTR9cTV9cTZ9cTd9cTh9cTllVQxhcm9tYXRpY01vZGVxOksGSwF9h3E7VQNpZHNxPEsGSwBLAIZ9cT0oSwNLAIZxPl1xP0sDYUsCSwCGcUBdcUFLAmFLBUsAhnFCXXFDSwVhSwFLAIZxRF1xRUsBYUsESwCGcUZdcUdLBGF1h3FIVQ5zdXJmYWNlT3BhY2l0eXFJSwZHv/AAAAAAAAB9h3FKVQlhdXRvY2hhaW5xS0sGiH2HcUxVCnZkd0RlbnNpdHlxTUsGR0AUAAAAAAAAfYdxTlUNYXJvbWF0aWNDb2xvcnFPSwZOfYdxUFUGaGlkZGVucVFLBol9h3FSVQlsaW5lV2lkdGhxU0sGRz/wAAAAAAAAfYdxVFUKc3RpY2tTY2FsZXFVSwZHP/AAAAAAAAB9h3FWVQdkaXNwbGF5cVdLBoh9h3FYVRBhcm9tYXRpY0xpbmVUeXBlcVlLBksCfYdxWnUu'))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksMVQEgfYdxA1ULZmlsbERpc3BsYXlxBEsMiX2HcQVVBG5hbWVxBksMVQFBfXEHVQFHXXEIKEsBSwNLBUsHSwlLC2Vzh3EJVQVjaGFpbnEKSwxVAUF9cQtVAUJOXXEMKEsBSwGGcQ1LA0sBhnEOSwVLAYZxD0sHSwGGcRBLCUsBhnERSwtLAYZxEmWGcRNzh3EUVQ5yaWJib25EcmF3TW9kZXEVSwxLAn2HcRZVAnNzcRdLDImJiYd9h3EYVQhtb2xlY3VsZXEZSwxLAH1xGihLAU5dcRtLAksChnEcYYZxHUsCTl1xHksESwKGcR9hhnEgSwNOXXEhSwZLAoZxImGGcSNLBE5dcSRLCEsChnElYYZxJksFTl1xJ0sKSwKGcShhhnEpdYdxKlULcmliYm9uQ29sb3JxK0sMTn2HcSxVBWxhYmVscS1LDFUAfYdxLlUKbGFiZWxDb2xvcnEvSwxOfYdxMFUIZmlsbE1vZGVxMUsMSwF9h3EyVQVpc0hldHEzSwyJfYdxNFULbGFiZWxPZmZzZXRxNUsMTn2HcTZVCHBvc2l0aW9ucTddcTgoSwFLAoZxOUsBSwKGcTpLAUsChnE7SwFLAoZxPEsBSwKGcT1LAUsChnE+ZVUNcmliYm9uRGlzcGxheXE/SwyJfYdxQFUIb3B0aW9uYWxxQX1xQlUEc3NJZHFDSwxK/////32HcUR1Lg=='))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVhdG9tc3ECXXEDKF1xBChLE0sSZV1xBShLE0sUZV1xBihLFUsUZV1xByhLFksVZV1xCChLFksSZV1xCShLFksXZV1xCihLGEsXZV1xCyhLGEsZZV1xDChLGksZZV1xDShLGksbZV1xDihLHEsbZV1xDyhLHUsbZV1xEChLFUsaZV1xEShLGEseZV1xEihLE0sfZV1xEyhLIEsSZV1xFChLIkshZV1xFShLIksjZV1xFihLJEsjZV1xFyhLJEslZV1xGChLJUsmZV1xGShLJ0smZV1xGihLJ0soZV1xGyhLKUsoZV1xHChLKUskZV1xHShLKUshZV1xHihLJ0sqZV1xHyhLK0sqZV1xIChLLEsqZV1xIShLLUsmZV1xIihLJUsuZV1xIyhLIksvZV1xJChLMEshZV1xJShLMksxZV1xJihLMkszZV1xJyhLNEszZV1xKChLNEs1ZV1xKShLNUs2ZV1xKihLN0s2ZV1xKyhLOEs2ZV1xLChLNUs5ZV1xLShLOks5ZV1xLihLOks7ZV1xLyhLOks8ZV1xMChLPUs8ZV1xMShLPUsxZV1xMihLPUs0ZV1xMyhLMks+ZV1xNChLP0sxZV1xNShLQUtAZV1xNihLQUtCZV1xNyhLQUtDZV1xOChLREtDZV1xOShLRUtEZV1xOihLRUtAZV1xOyhLRUtGZV1xPChLR0tGZV1xPShLR0tIZV1xPihLSUtIZV1xPyhLSktIZV1xQChLR0tLZV1xQShLTEtLZV1xQihLREtMZV1xQyhLTEtNZV1xRChLTktLZV1xRShLT0tAZV1xRihLUUtQZV1xRyhLUUtSZV1xSChLUUtTZV1xSShLVEtTZV1xSihLVEtVZV1xSyhLVUtWZV1xTChLV0tWZV1xTShLV0tYZV1xTihLV0tZZV1xTyhLWktZZV1xUChLWktQZV1xUShLWktUZV1xUihLVUtbZV1xUyhLXEtbZV1xVChLXUtbZV1xVShLXktQZV1xVihLYEtfZV1xVyhLYEthZV1xWChLYkthZV1xWShLY0tiZV1xWihLY0tfZV1xWyhLY0tkZV1xXChLZUtkZV1xXShLZUtmZV1xXihLZ0tmZV1xXyhLZ0toZV1xYChLYktnZV1xYShLaUtmZV1xYihLZUtqZV1xYyhLa0tqZV1xZChLbEtqZV1xZShLYEttZV1xZihLbktfZV1xZyhLcEtvZV1xaChLcEtxZV1xaShLcktxZV1xaihLcktzZV1xayhLc0t0ZV1xbChLdUt0ZV1xbShLdUt2ZV1xbihLdUt3ZV1xbyhLeEt3ZV1xcChLeEtvZV1xcShLeEtyZV1xcihLc0t5ZV1xcyhLekt5ZV1xdChLe0t5ZV1xdShLcEt8ZV1xdihLfUtvZV1xdyhLf0t+ZV1xeChLgEt+ZV1xeShLgEuBZV1xeihLgkuBZV1xeyhLgkuDZV1xfChLhEuDZV1xfShLhUuDZV1xfihLgkuGZV1xfyhLh0uGZV1xgChLh0uIZV1xgShLiUuHZV1xgihLgEuJZV1xgyhLiUuKZV1xhChLi0uKZV1xhShLi0t+ZV1xhihLi0uMZV1xhyhLjUuGZV1xiChLj0uOZV1xiShLkEuOZV1xiihLkEuRZV1xiyhLkkuRZV1xjChLkkuTZV1xjShLk0uUZV1xjihLlUuUZV1xjyhLlUuWZV1xkChLlUuXZV1xkShLmEuXZV1xkihLmEuOZV1xkyhLmEuSZV1xlChLk0uZZV1xlShLmkuZZV1xlihLm0uZZV1xlyhLkEucZV1xmChLnkudZV1xmShLnkufZV1xmihLn0ugZV1xmyhLoEuhZV1xnChLoEuiZV1xnShLo0uiZV1xnihLpEuiZV1xnyhLpEulZV1xoChLnkulZV1xoShLpEumZV1xoihLp0umZV1xoyhLqEumZV1xpChLn0upZV1xpShLqkupZV1xpihLqkurZV1xpyhLqkudZV1xqChLrEudZV1xqShLrkutZV1xqihLrkuvZV1xqyhLsEuvZV1xrChLsEuxZV1xrShLsEuyZV1xrihLs0uyZV1xryhLs0u0ZV1xsChLtUu0ZV1xsShLtku0ZV1xsihLt0uzZV1xsyhLt0u4ZV1xtChLuUu4ZV1xtShLuUu6ZV1xtihLuUutZV1xtyhLrku3ZV1xuChLu0utZV1xuShLvUu8ZV1xuihLvku8ZV1xuyhLvku/ZV1xvChLv0vAZV1xvShLwEvBZV1xvihLwkvBZV1xvyhLw0vBZV1xwChLw0vEZV1xwShLxUvEZV1xwihLxkvEZV1xwyhLw0vHZV1xxChLvkvHZV1xxShLwEvIZV1xxihLv0vJZV1xxyhLykvJZV1xyChLyku8ZV1xyShLykvLZWVVBWxhYmVsccpLxlUAfYdxy1UGcmFkaXVzccxLxkc/yZmZoAAAAH2Hcc1VC2xhYmVsT2Zmc2V0cc5Lxk59h3HPVQhkcmF3TW9kZXHQS8ZLAX2HcdFVCG9wdGlvbmFscdJ9cdNVB2Rpc3BsYXlx1EvGSwJ9h3HVdS4='))
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
	pbInfo = {'category': ['distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 9, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = {0: ('_openColor00', (1, 1, 1, 1)), 1: ('_openColor01', (1, 0, 1, 1)), 2: ('_openColor02', (0, 1, 1, 1)), 3: ('_openColor03', (1, 1, 0, 1)), 4: ('_openColor04', (1, 0, 0, 1)), 5: ('_openColor05', (0, 0, 1, 1)), 6: ('N', (0.188235, 0.313725, 0.972549, 1)), 7: ('H', (1, 1, 1, 1)), 8: ('O', (1, 0.0509804, 0.0509804, 1)), 9: ('yellow', (1, 1, 0, 1)), 10: ('white', (1, 1, 1, 1)), 11: ('green', (0, 1, 0, 1))}
	viewerInfo = {'cameraAttrs': {'center': (8.3885, 15.1655, 37.3352), 'fieldOfView': 26.2751, 'nearFar': (46.2043, 27.8414), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 37.076}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'viewSize': 11.614, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 1, 'depthCue': True, 'highlight': 0, 'scaleFactor': 0.820621}, 'viewerHL': 11, 'cameraMode': 'mono', 'detail': 1, 'viewerFog': None, 'viewerBG': 10}

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
	residueData = [(6, 'Chimera default', 'rounded', 'unknown'), (7, 'Chimera default', 'rounded', 'unknown'), (8, 'Chimera default', 'rounded', 'unknown'), (9, 'Chimera default', 'rounded', 'unknown'), (10, 'Chimera default', 'rounded', 'unknown'), (11, 'Chimera default', 'rounded', 'unknown'), (12, 'Chimera default', 'rounded', 'unknown'), (13, 'Chimera default', 'rounded', 'unknown'), (14, 'Chimera default', 'rounded', 'unknown'), (15, 'Chimera default', 'rounded', 'unknown'), (16, 'Chimera default', 'rounded', 'unknown'), (17, 'Chimera default', 'rounded', 'unknown')]
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
	xformMap = {0: (((-0.768847, -0.492936, -0.407295), 87.5059), (-2.97384, -23.7794, 30.7727), True), 1: (((-0.654695, 0.478405, 0.585238), 150.274), (9.40302, 15.3062, 40.5292), True), 2: (((-0.45518, -0.824351, -0.336537), 121.039), (24.0293, 6.53266, 14.8503), True), 3: (((0.0883338, -0.723864, 0.684265), 127.882), (23.9052, 14.6091, 14.1209), True), 4: (((0.64599, -0.761267, -0.0563033), 178.339), (21.391, 9.56821, 48.0205), True), 5: (((0.71734, -0.18356, 0.672108), 129.314), (4.97848, 9.9116, 19.9827), True)}
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

