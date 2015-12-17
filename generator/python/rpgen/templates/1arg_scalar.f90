{#
  Copyright 2015 Andrew Dawson, Peter Dueben

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
#}
    FUNCTION {{ function.name }}_{{ type1.name }} (a) RESULT (x)
        {{ type1.declaration }}, INTENT(IN) :: a
        {{ function.return_type.declaration }} :: x
        {% if function.return_type.name == "rpe" %}
        x%sbits = significand_bits(a)
        {% endif %}
        x = {{ function.name.upper() }}(a{{ type1.accessor }})
    END FUNCTION {{ function.name }}_{{ type1.name }}
