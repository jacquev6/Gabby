import TextPicker from './TextPicker.vue'


// Actual content from exercise 3 in test.pdf
const textContent = [
  {
    "str": "",
    "font": "g_d0_f11",
    "left": 15.408400000000029,
    "width": 0,
    "right": 15.408400000000029,
    "bottom": 104.34909999999999,
    "height": 0,
    "top": 104.34909999999999
  },
  {
    "str": "3",
    "font": "g_d0_f11",
    "left": 15.408400000000029,
    "width": 6.492245200000001,
    "right": 21.900645200000042,
    "bottom": 104.34909999999999,
    "height": 11.6767,
    "top": 116.02579999999998
  },
  {
    "str": " ",
    "font": "g_d0_f11",
    "left": 21.900645200000042,
    "width": 1.4357784990622353,
    "right": 23.336423699062266,
    "bottom": 104.34909999999999,
    "height": 0,
    "top": 104.34909999999999
  },
  {
    "str": "Complète avec",
    "font": "g_d0_f2",
    "left": 38.66580000000005,
    "width": 80.02375000000008,
    "right": 118.68955000000011,
    "bottom": 103.2363,
    "height": 12.5,
    "top": 115.7363
  },
  {
    "str": " ",
    "font": "g_d0_f2",
    "left": 118.68955000000005,
    "width": 0.12509999999999763,
    "right": 118.81465000000003,
    "bottom": 103.2363,
    "height": 0,
    "top": 103.2363
  },
  {
    "str": ":",
    "font": "g_d0_f2",
    "left": 120.25330000000002,
    "width": 3.4750000000000005,
    "right": 123.72830000000005,
    "bottom": 103.2363,
    "height": 12.5,
    "top": 115.7363
  },
  {
    "str": " ",
    "font": "g_d0_f2",
    "left": 123.72830000000005,
    "width": 0.2059999999999991,
    "right": 123.93430000000006,
    "bottom": 103.2363,
    "height": 0,
    "top": 103.2363
  },
  {
    "str": "le",
    "font": "g_d0_f12",
    "left": 126.30330000000004,
    "width": 9.25,
    "right": 135.55330000000004,
    "bottom": 103.2363,
    "height": 12.5,
    "top": 115.7363
  },
  {
    "str": ",",
    "font": "g_d0_f2",
    "left": 135.55330000000004,
    "width": 3.4000000000000004,
    "right": 138.9533,
    "bottom": 103.2363,
    "height": 12.5,
    "top": 115.7363
  },
  {
    "str": " ",
    "font": "g_d0_f2",
    "left": 138.9533,
    "width": 0.2059999999999991,
    "right": 139.15930000000003,
    "bottom": 103.2363,
    "height": 0,
    "top": 103.2363
  },
  {
    "str": "une",
    "font": "g_d0_f12",
    "left": 141.5283,
    "width": 19.687500000000004,
    "right": 161.2158,
    "bottom": 103.2363,
    "height": 12.5,
    "top": 115.7363
  },
  {
    "str": ",",
    "font": "g_d0_f2",
    "left": 161.21580000000006,
    "width": 3.4000000000000004,
    "right": 164.61580000000004,
    "bottom": 103.2363,
    "height": 12.5,
    "top": 115.7363
  },
  {
    "str": " ",
    "font": "g_d0_f2",
    "left": 164.61580000000004,
    "width": 0.2059999999999991,
    "right": 164.82180000000005,
    "bottom": 103.2363,
    "height": 0,
    "top": 103.2363
  },
  {
    "str": "un",
    "font": "g_d0_f12",
    "left": 167.19080000000002,
    "width": 13.525,
    "right": 180.7158,
    "bottom": 103.2363,
    "height": 12.5,
    "top": 115.7363
  },
  {
    "str": ",",
    "font": "g_d0_f2",
    "left": 180.71580000000006,
    "width": 3.4000000000000004,
    "right": 184.11580000000004,
    "bottom": 103.2363,
    "height": 12.5,
    "top": 115.7363
  },
  {
    "str": " ",
    "font": "g_d0_f2",
    "left": 184.11580000000004,
    "width": 0.2059999999999991,
    "right": 184.32180000000005,
    "bottom": 103.2363,
    "height": 0,
    "top": 103.2363
  },
  {
    "str": "des",
    "font": "g_d0_f12",
    "left": 186.69080000000002,
    "width": 17.875000000000025,
    "right": 204.56580000000008,
    "bottom": 103.2363,
    "height": 12.5,
    "top": 115.7363
  },
  {
    "str": ",",
    "font": "g_d0_f2",
    "left": 204.56580000000008,
    "width": 3.4000000000000004,
    "right": 207.96580000000006,
    "bottom": 103.2363,
    "height": 12.5,
    "top": 115.7363
  },
  {
    "str": " ",
    "font": "g_d0_f2",
    "left": 207.96580000000006,
    "width": 0.20600000000000362,
    "right": 208.17180000000008,
    "bottom": 103.2363,
    "height": 0,
    "top": 103.2363
  },
  {
    "str": "tu",
    "font": "g_d0_f12",
    "left": 210.5408000000001,
    "width": 10.862500000000024,
    "right": 221.40330000000017,
    "bottom": 103.2363,
    "height": 12.5,
    "top": 115.7363
  },
  {
    "str": ",",
    "font": "g_d0_f2",
    "left": 221.40330000000006,
    "width": 3.4000000000000004,
    "right": 224.80330000000004,
    "bottom": 103.2363,
    "height": 12.5,
    "top": 115.7363
  },
  {
    "str": "",
    "font": "g_d0_f12",
    "left": 10.003300000000081,
    "width": 0,
    "right": 10.003300000000081,
    "bottom": 88.2113,
    "height": 0,
    "top": 88.2113
  },
  {
    "str": "elles",
    "font": "g_d0_f12",
    "left": 10.003300000000081,
    "width": 23.162500000000026,
    "right": 33.165800000000104,
    "bottom": 88.2113,
    "height": 12.5,
    "top": 100.71130000000002
  },
  {
    "str": ",",
    "font": "g_d0_f2",
    "left": 33.165800000000104,
    "width": 3.4000000000000004,
    "right": 36.56580000000008,
    "bottom": 88.2113,
    "height": 12.5,
    "top": 100.71130000000002
  },
  {
    "str": " ",
    "font": "g_d0_f2",
    "left": 36.56580000000008,
    "width": 0.2059999999999991,
    "right": 36.7718000000001,
    "bottom": 88.2113,
    "height": 0,
    "top": 88.2113
  },
  {
    "str": "ils",
    "font": "g_d0_f12",
    "left": 39.14080000000007,
    "width": 11,
    "right": 50.14080000000007,
    "bottom": 88.2113,
    "height": 12.5,
    "top": 100.71130000000002
  },
  {
    "str": ". Puis, souligne les verbes.",
    "font": "g_d0_f2",
    "left": 50.14080000000007,
    "width": 139.76125,
    "right": 189.90205000000003,
    "bottom": 88.2113,
    "height": 12.5,
    "top": 100.71130000000002
  },
  {
    "str": "",
    "font": "g_d0_f6",
    "left": 92.46850000000006,
    "width": 0,
    "right": 92.46850000000006,
    "bottom": 66.45930000000001,
    "height": 0,
    "top": 66.45930000000001
  },
  {
    "str": "Il peut y avoir plusieurs",
    "font": "g_d0_f6",
    "left": 92.46850000000006,
    "width": 102.33079999999994,
    "right": 194.79930000000002,
    "bottom": 66.45930000000001,
    "height": 11,
    "top": 77.45930000000001
  },
  {
    "str": "solutions.",
    "font": "g_d0_f6",
    "left": 92.46850000000006,
    "width": 41.734,
    "right": 134.20250000000004,
    "bottom": 54.45830000000001,
    "height": 11,
    "top": 65.45830000000001
  },
  {
    "str": "",
    "font": "g_d0_f8",
    "left": 10.003500000000031,
    "width": 0,
    "right": 10.003500000000031,
    "bottom": 25.025000000000006,
    "height": 0,
    "top": 25.025000000000006
  },
  {
    "str": "…",
    "font": "g_d0_f8",
    "left": 10.003500000000031,
    "width": 12.425,
    "right": 22.428500000000042,
    "bottom": 25.025000000000006,
    "height": 12.5,
    "top": 37.525000000000006
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 22.428500000000042,
    "width": 0.09699999999999818,
    "right": 22.525500000000022,
    "bottom": 25.025000000000006,
    "height": 0,
    "top": 25.025000000000006
  },
  {
    "str": "vide",
    "font": "g_d0_f8",
    "left": 23.64100000000002,
    "width": 19.54999999999998,
    "right": 43.190999999999974,
    "bottom": 25.025000000000006,
    "height": 12.5,
    "top": 37.525000000000006
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 43.190999999999974,
    "width": 0.09322307692308239,
    "right": 43.28422307692307,
    "bottom": 25.025000000000006,
    "height": 0,
    "top": 25.025000000000006
  },
  {
    "str": "◆",
    "font": "g_d0_f8",
    "left": 44.402900000000045,
    "width": 5.902,
    "right": 50.30490000000003,
    "bottom": 25.025000000000006,
    "height": 13,
    "top": 38.025000000000006
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 50.30490000000003,
    "width": 0.09459199999999783,
    "right": 50.39949200000001,
    "bottom": 25.025000000000006,
    "height": 0,
    "top": 25.025000000000006
  },
  {
    "str": "…",
    "font": "g_d0_f8",
    "left": 51.487300000000005,
    "width": 12.425,
    "right": 63.912300000000016,
    "bottom": 25.025000000000006,
    "height": 12.5,
    "top": 37.525000000000006
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 63.912300000000016,
    "width": 0.09699999999999818,
    "right": 64.0093,
    "bottom": 25.025000000000006,
    "height": 0,
    "top": 25.025000000000006
  },
  {
    "str": "vident",
    "font": "g_d0_f8",
    "left": 65.1248,
    "width": 28.09999999999996,
    "right": 93.22479999999996,
    "bottom": 25.025000000000006,
    "height": 12.5,
    "top": 37.525000000000006
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 93.22479999999996,
    "width": 0.09321538461539201,
    "right": 93.31801538461536,
    "bottom": 25.025000000000006,
    "height": 0,
    "top": 25.025000000000006
  },
  {
    "str": "◆",
    "font": "g_d0_f8",
    "left": 94.43660000000006,
    "width": 5.902,
    "right": 100.33860000000004,
    "bottom": 25.025000000000006,
    "height": 13,
    "top": 38.025000000000006
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 100.33860000000004,
    "width": 0.10087199999999939,
    "right": 100.43947200000002,
    "bottom": 25.025000000000006,
    "height": 0,
    "top": 25.025000000000006
  },
  {
    "str": "…",
    "font": "g_d0_f8",
    "left": 101.59950000000003,
    "width": 12.425,
    "right": 114.02450000000005,
    "bottom": 25.025000000000006,
    "height": 12.5,
    "top": 37.525000000000006
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 114.02450000000005,
    "width": 0.09699999999999818,
    "right": 114.12150000000003,
    "bottom": 25.025000000000006,
    "height": 0,
    "top": 25.025000000000006
  },
  {
    "str": "dépenses",
    "font": "g_d0_f8",
    "left": 115.23700000000002,
    "width": 42.51125000000005,
    "right": 157.7482500000001,
    "bottom": 25.025000000000006,
    "height": 12.5,
    "top": 37.525000000000006
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 157.74824999999998,
    "width": 0.09329615384615846,
    "right": 157.84154615384614,
    "bottom": 25.025000000000006,
    "height": 0,
    "top": 25.025000000000006
  },
  {
    "str": "◆",
    "font": "g_d0_f8",
    "left": 158.96110000000004,
    "width": 5.902,
    "right": 164.86310000000003,
    "bottom": 25.025000000000006,
    "height": 13,
    "top": 38.025000000000006
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 164.86310000000003,
    "width": 0.1008640000000014,
    "right": 164.96396400000003,
    "bottom": 25.025000000000006,
    "height": 0,
    "top": 25.025000000000006
  },
  {
    "str": "…",
    "font": "g_d0_f8",
    "left": 166.12390000000005,
    "width": 12.425,
    "right": 178.54890000000006,
    "bottom": 25.025000000000006,
    "height": 12.5,
    "top": 37.525000000000006
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 178.54890000000006,
    "width": 0.09699999999999818,
    "right": 178.64590000000004,
    "bottom": 25.025000000000006,
    "height": 0,
    "top": 25.025000000000006
  },
  {
    "str": "dépensent",
    "font": "g_d0_f8",
    "left": 179.76140000000004,
    "width": 47.561250000000165,
    "right": 227.32265000000018,
    "bottom": 25.025000000000006,
    "height": 12.5,
    "top": 37.525000000000006
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 227.3226500000003,
    "width": 0.09330384615382697,
    "right": 227.41595384615414,
    "bottom": 25.025000000000006,
    "height": 0,
    "top": 25.025000000000006
  },
  {
    "str": "◆",
    "font": "g_d0_f8",
    "left": 228.53560000000004,
    "width": 5.902,
    "right": 234.4376000000001,
    "bottom": 25.025000000000006,
    "height": 13,
    "top": 38.025000000000006
  },
  {
    "str": "…",
    "font": "g_d0_f8",
    "left": 10,
    "width": 12.425,
    "right": 22.42500000000001,
    "bottom": 10,
    "height": 12.5,
    "top": 22.5
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 22.42500000000001,
    "width": 0.09699999999999818,
    "right": 22.52199999999999,
    "bottom": 10,
    "height": 0,
    "top": 10
  },
  {
    "str": "savon",
    "font": "g_d0_f8",
    "left": 23.63749999999999,
    "width": 25.375000000000014,
    "right": 49.01249999999999,
    "bottom": 10,
    "height": 12.5,
    "top": 22.5
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 49.01249999999999,
    "width": 0.09347692307692604,
    "right": 49.10597692307692,
    "bottom": 10,
    "height": 0,
    "top": 10
  },
  {
    "str": "◆",
    "font": "g_d0_f8",
    "left": 50.22770000000003,
    "width": 5.902,
    "right": 56.129700000000014,
    "bottom": 10.00200000000001,
    "height": 13,
    "top": 23.00200000000001
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 56.129700000000014,
    "width": 0.09459200000000237,
    "right": 56.22429199999999,
    "bottom": 10.00200000000001,
    "height": 0,
    "top": 10.00200000000001
  },
  {
    "str": "…",
    "font": "g_d0_f8",
    "left": 57.312100000000044,
    "width": 12.425,
    "right": 69.73710000000005,
    "bottom": 10.00200000000001,
    "height": 12.5,
    "top": 22.50200000000001
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 69.73710000000005,
    "width": 0.09699999999999818,
    "right": 69.83410000000003,
    "bottom": 10.00200000000001,
    "height": 0,
    "top": 10.00200000000001
  },
  {
    "str": "savons",
    "font": "g_d0_f8",
    "left": 70.94960000000003,
    "width": 28.99875000000001,
    "right": 99.94835000000006,
    "bottom": 10.00200000000001,
    "height": 12.5,
    "top": 22.50200000000001
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 99.94835,
    "width": 0.09330384615384883,
    "right": 100.04165384615385,
    "bottom": 10.00200000000001,
    "height": 0,
    "top": 10.00200000000001
  },
  {
    "str": "◆",
    "font": "g_d0_f8",
    "left": 101.16130000000004,
    "width": 5.902,
    "right": 107.06330000000003,
    "bottom": 10.00200000000001,
    "height": 13,
    "top": 23.00200000000001
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 107.06330000000003,
    "width": 0.09459199999999783,
    "right": 107.157892,
    "bottom": 10.00200000000001,
    "height": 0,
    "top": 10.00200000000001
  },
  {
    "str": "…",
    "font": "g_d0_f8",
    "left": 108.2457,
    "width": 12.425,
    "right": 120.67070000000001,
    "bottom": 10.00200000000001,
    "height": 12.5,
    "top": 22.50200000000001
  },
  {
    "str": " ",
    "font": "g_d0_f8",
    "left": 120.67070000000001,
    "width": 0.09699999999999818,
    "right": 120.76769999999999,
    "bottom": 10.00200000000001,
    "height": 0,
    "top": 10.00200000000001
  },
  {
    "str": "commande",
    "font": "g_d0_f8",
    "left": 121.88319999999999,
    "width": 50.49874999999997,
    "right": 172.38194999999996,
    "bottom": 10.00200000000001,
    "height": 12.5,
    "top": 22.50200000000001
  }
]

describe('TextPicker', () => {
  it('picks text', () => {
    const onTextSelectedSpy = cy.spy().as('onTextSelectedSpy')

    cy.mount(TextPicker, {props: {
      width: 410, height: 297,
      transform: [1, 0, 0, 1, 0, 0],
      textContent,
      onTextSelected: onTextSelectedSpy
    }})

    const canvas = cy.get('canvas')
    canvas.trigger('pointermove', 2, 2)
    canvas.trigger('pointerdown', 2, 2, { pointerId: 1 })
    canvas.trigger('pointermove', 340, 155)
    canvas.trigger('pointerup', 340, 155, { pointerId: 1 })

    cy.get('@onTextSelectedSpy').should(
      'have.been.calledWith',
      {
        "withoutLineEnds": "3 Complète avec : le, une, un, des, tu, elles, ils. Puis, souligne les verbes.\nIl peut y avoir plusieurs solutions.\n... vide ◆ ... vident ◆ ... dépenses ◆ ... dépensent ◆ ... savon ◆ ... savons ◆ ... commande\n",
        "withAllLineEnds": "3 Complète avec : le, une, un, des, tu,\nelles, ils. Puis, souligne les verbes.\nIl peut y avoir plusieurs\nsolutions.\n... vide ◆ ... vident ◆ ... dépenses ◆ ... dépensent ◆\n... savon ◆ ... savons ◆ ... commande\n",
        "withoutListsDetection": "3 Complète avec : le, une, un, des, tu, elles, ils. Puis, souligne les verbes.\nIl peut y avoir plusieurs solutions.\n... vide ◆ ... vident ◆ ... dépenses ◆ ... dépensent ◆ ... savon ◆ ... savons ◆ ... commande\n"
      },
      {'clientX': 348, 'clientY': 163},
    )
  })
})
